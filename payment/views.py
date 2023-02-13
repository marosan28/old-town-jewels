from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
import os
import stripe
from decimal import Decimal
from orders.models import Order
from django.urls import reverse
from django.conf import settings
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment_method = request.POST.get('payment_method')
    print('Payment method:', payment_method)
    if request.method == 'POST':
        session_data = {
            'payment_method_types': ['card'],
            'client_reference_id': order.id,
            'line_items': [],
            'mode': 'payment',
            'success_url': request.build_absolute_uri(reverse('payment:completed')),
            'cancel_url': request.build_absolute_uri(reverse('payment:canceled'))
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
        return redirect('payment:form', order_id=order_id, session_id=session_id)
    else:
        return render(request, 'payment/process.html', {'order': order})

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def payment_form(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()
    total = order.get_total_cost()

    # Get or create a PaymentIntent
    payment_intent_id = order.payment_intent_id
    if payment_intent_id is None:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total * 100),
            currency='eur',
            payment_method_types=['card'],
            customer_email=request.user.email,
            metadata={
                'order_id': order.id
            }
        )
        payment_intent_id = payment_intent.id
        order.payment_intent_id = payment_intent_id
        order.save()
    else:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

    # Render the payment form with the client_secret and other necessary details
    return render(request, 'payment/payment_form.html', {
        'order_id': order_id,
        'payment_intent_id': payment_intent_id,
        'client_secret': payment_intent.client_secret,
        'order_items': order_items,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

intent = stripe.PaymentIntent.create(
    amount=1000,
    currency="eur",
)

client_secret = intent.client_secret

    
