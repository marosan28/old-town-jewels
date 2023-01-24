from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('register/', views.register, name='register'),
    path('users/logout/', views.logout_view, name='logout'),
    path('subscribe', views.subscribe, name='subscribe'),
]
