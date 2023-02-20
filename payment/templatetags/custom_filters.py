from django import template

register = template.Library()

@register.filter(name='total_price')
def total_price(item):
    return item.price * item.quantity
