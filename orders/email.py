from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from orders.models import Order

def send_confirmation_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order Confirmation for Order #{}'.format(order.id)
    html_message = render_to_string('orders/confirmation_email.html', {'order': order})
    plain_message = strip_tags(html_message)
    from_email = 'no-reply@old-town-jewels.herokuapp.com'
    recipient_list = [order.email]
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
