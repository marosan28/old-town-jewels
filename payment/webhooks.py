import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import os
from orders.models import Order

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
                    payload,
                    sig_header,
                    settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # mark order as paid
            order.paid = True
            # store Stripe payment ID
            order.stripe_id = session.payment_intent
            order.save()
            
            # send order confirmation email
            email_subject = "Old Town Jewels: Order Confirmation"
            email_body = "Your order with Order Number: {0} has been placed successfully. Total Amount: {1}. Date: {2}.\n\nOrder Details:\n\n".format(
                order.id, order.total_amount, order.ordered_date)
            for item in order.items.all():
                email_body += "\tProduct Name: {0}\t Quantity: {1}\t Price: {2}\n".format(
                    item.product.name, item.quantity, item.price)

            email_body += "\nThank you for your purchase!\n\nBest regards,\nThe Old Town Jewels Team"
            from_email = os.environ.get('DEFAULT_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
            recipient_list = [order.email]
            send_mail(email_subject, email_body, from_email, recipient_list)

    return HttpResponse(status=200)
