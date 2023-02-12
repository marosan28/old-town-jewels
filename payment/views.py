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

    if request.method == 'POST':
        success_url = "https://8000-marosan28-oldtownjewels-tvocoizkdq5.ws-eu86.gitpod.io/payment/completed/"
        cancel_url = request.build_absolute_uri(
                        reverse('payment:canceled'))

        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'eur',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })
        # Stripe coupon
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                                name=order.coupon.code,
                                percent_off=order.discount,
                                duration='once')
            session_data['discounts'] = [{
                'coupon': stripe_coupon.id
            }]
        
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        session_id = session.id

        # redirect the user to the payment_form view
        return redirect('payment:payment_form', order_id=order_id, session_id=session_id)

    else:
        return render(request, 'payment/process.html', locals())

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def payment_form(request, order_id, session_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()

    first_name = request.session.get('first_name', '')
    last_name = request.session.get('last_name', '')
    email = request.session.get('email', '')
    address = request.session.get('address', '')
    postal_code = request.session.get('postal_code', '')
    city = request.session.get('city', '')

    return render(request, 'payment/payment_form.html', {
        'order_id': order_id,
        'session_id': session_id,
        'order_items': order_items,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'postal_code': postal_code,
        'city': city,
        'show_subheader': False,
    })


    
