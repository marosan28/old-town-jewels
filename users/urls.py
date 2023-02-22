from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView, LoginView, PasswordChangeView
from .import views

app_name = 'users'
urlpatterns = [
    # Django's built-in authentication URLs
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('users/logout/', views.logout_view, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),


    # password change URLs
    path('password-change/', PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
