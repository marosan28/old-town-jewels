from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
import os
import stripe
from decimal import Decimal
from orders.models import Order
from django.urls import reverse
from django.conf import settings
from cart.cart import Cart
from delivery.models import DeliveryOption
from django_countries import countries
from .forms import EmailPostForm
from django.http import HttpResponse
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def update_delivery_charge(request):
    if request.method == 'POST':
        delivery_charge = request.POST.get('delivery_charge', 0)
        request.session['delivery_charge'] = delivery_charge
        return JsonResponse({'message': 'Delivery charge updated in session'})

    return JsonResponse({'message':
                         'Error updating delivery charge in session'})


def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment_method = request.POST.get('payment_method')

    if request.method == 'POST':
        session_data = {
            'payment_method_types': ['card'],
            'client_reference_id': order.id,
            'line_items': [],
            'mode': 'payment',
            'success_url': request.build_absolute_uri(
                reverse('payment:completed')),
            'cancel_url': request.build_absolute_uri(
                reverse('payment:canceled'))
        }

        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': int(item.price * 100),
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })

        # Add a line item for the delivery charge
        delivery_charge = request.session.get('delivery_charge', 0)
        if delivery_charge:
            delivery_charge = float(delivery_charge)
            session_data['line_items'].append({
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': int(delivery_charge * 100),
                    'product_data': {
                        'name': 'Delivery Charge',
                    },
                },
                'quantity': 1,
            })

        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                name=order.coupon.code,
                percent_off=order.discount,
                duration='once'
            )
            session_data['discounts'] = [{
                'coupon': stripe_coupon.id
            }]

        session = stripe.checkout.Session.create(**session_data)
        session_id = session.id
        request.session['order_id'] = order_id
        return redirect('payment:payment_form',
                        order_id=order_id,
                        session_id=session_id)

    else:
        return render(request, 'payment/process.html', {'order': order})


def payment_completed(request):
    order_id = request.session.get('order_id')
    order = Order.objects.get(id=order_id)
    delivery_charge = request.session.get('delivery_charge', 0)
    total_cost = order.get_total_cost() + Decimal(str(delivery_charge))
    order_items = order.items.all()
    coupon_code = order.coupon.code if order.coupon else None

    # Get the PaymentIntent and extract payment method and transaction ID
    payment_intent = stripe.PaymentIntent.retrieve(order.payment_intent_id)
    payment_method = payment_intent.payment_method
    transaction_id = payment_intent.id

    # Retrieve more details about the payment method
    payment_method_details = stripe.PaymentMethod.retrieve(payment_method).card
    payment_method_type = payment_method_details.brand.title()
    payment_method_last4 = payment_method_details.last4

    order.paid_date = timezone.now()
    order.save()

    send_order_confirmation_email(order_id, delivery_charge, total_cost,
                                  order_items, coupon_code, payment_method,
                                  transaction_id, order.email)

    return render(request, 'payment/completed.html', {
        'order': order,
        'delivery_charge': delivery_charge,
        'total_cost': total_cost,
        'order_items': order_items,
        'coupon_code': coupon_code,
        'payment_method': payment_method,
        'transaction_id': transaction_id,
        'payment_method_type': payment_method_type,
        'payment_method_last4': payment_method_last4
    })


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_form(request, order_id, session_id):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()
    delivery_charge = request.session.get('delivery_charge', 0)
    request.session['delivery_charge'] = delivery_charge
    total = order.get_total_cost() + Decimal(str(delivery_charge))
    address = request.session.get('address')
    address2 = request.session.get('address2')
    postal_code = request.session.get('postal_code')
    city = request.session.get('city')
    shipping_country = request.session.get('shipping_country')

    # Get or create a PaymentIntent
    payment_intent_id = order.payment_intent_id
    if payment_intent_id is None:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total * 100),
            currency='eur',
            payment_method_types=['card'],
            metadata={
                'order_id': order.id,
                'email': request.user.email
            }
        )
        payment_intent_id = payment_intent.id
        order.payment_intent_id = payment_intent_id
        order.save()
    else:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        customer_email = payment_intent.metadata.get('email')
    delivery_options = DeliveryOption.objects.all()
    return render(request, 'payment/payment_form.html', {
        'order_id': order_id,
        'payment_intent_id': payment_intent_id,
        'client_secret': payment_intent.client_secret,
        'order_items': order_items,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'address': address,
        'address2': address2,
        'postal_code': postal_code,
        'city': city,
        'shipping_country': shipping_country,
        'delivery_options': delivery_options,
        'delivery_charge': delivery_charge,
        'coupon_code': order.coupon.code if order.coupon else None,
    })


intent = stripe.PaymentIntent.create(
    amount=1000,
    currency="eur",
)

client_secret = intent.client_secret


def send_order_confirmation_email(order_id, delivery_charge, total_cost,
                                  order_items, coupon_code, payment_method_id,
                                  transaction_id, email):
    order = Order.objects.get(id=order_id)
    subject = 'Order Confirmation'

    message = f'Thank you for your order. Your order number is {order.id}.\n\n'
    message += 'Order summary:\n'

    for item in order_items:
        item_total = item.price * item.quantity
        item_summary = (
            f'{item.product.name} x {item.quantity} - '
            f'{item_total}\n'
        )
        message += item_summary

    message += f'Delivery charge: {delivery_charge}\n'
    message += f'Total cost: {total_cost}\n'

    if coupon_code:
        message += f'Coupon code: {coupon_code}\n'

    payment_method = stripe.PaymentMethod.retrieve(payment_method_id)
    message += f'Payment method: {payment_method.card.brand}\n'
    message += f'Transaction ID: {transaction_id}\n'

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)
