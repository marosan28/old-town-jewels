from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordChangeDoneView, LoginView, PasswordChangeView, PasswordResetDoneView, 
PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView)
from .import views
from .views import MyPasswordChangeView, MyPasswordChangeDoneView, MyPasswordResetDoneView, MyPasswordResetView, MyPasswordResetCompleteView, MyPasswordResetConfirmView

app_name = 'users'
urlpatterns = [
    # Django's built-in authentication URLs
    path('users/', include('django.contrib.auth.urls')),
    # Registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('edit/', views.edit, name='edit'),


    # password change URLs
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
