from django.urls import path, include
from .import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView
app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('register/', views.register, name='register'),
    path('users/logout/', views.logout_view, name='logout'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
