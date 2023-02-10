from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
import os
import stripe
from decimal import Decimal
from orders.models import Order
from django.urls import reverse
from django.conf import settings
import sendgrid
from sendgrid.helpers.mail import *

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION
sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        success_url = "https://8000-marosan28-oldtownjewels-e76llnxuqig.ws-eu86.gitpod.io/payment/completed/"
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
        email = request.POST.get('email')
        if email:
            email_body = ""
            email_subject = "Old Town Jewels: Order Confirmation"
            email_body = "Your order with Order Number: {0} has been placed successfully. Total Amount: {1}. Date: {2}.\n\nOrder Details:\n\n".format(
                order.id, order.total_amount, order.ordered_date)
        for item in order.items.all():
            email_body += "\tProduct Name: {0}\t Quantity: {1}\t Price: {2}\n".format(
                item.product.name, item.quantity, item.price)

            email_body += "\nThank you for your purchase!\n\nBest regards,\nThe Old Town Jewels Team"
            from_email = os.environ.get('DEFAULT_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
            recipient_list = [email]
    
            sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            from_email = Email(from_email)
            to_email = Email(recipient_list[0])
            subject = email_subject
            content = Content("text/plain", email_body)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            if response.status_code == 202:
                print("Email sent successfully")
            else:
                print("Failed to send email")


        return redirect(session.url, code=303)

    else:
        return render(request, 'payment/process.html', locals())

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
