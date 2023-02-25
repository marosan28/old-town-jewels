from django.urls import path
from . import views
from . import webhooks

app_name = 'payment'

urlpatterns = [
    path('process/<int:order_id>/', views.payment_process, name='process'),
    path('form/<int:order_id>/<str:session_id>/',
         views.payment_form, name='payment_form'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
    path('update_delivery_charge/', views.update_delivery_charge,
         name='update_delivery_charge')
]
