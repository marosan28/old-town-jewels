from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView, LoginView, PasswordChangeView
from .import views
from .views import MyPasswordChangeView, MyPasswordChangeDoneView

app_name = 'users'
urlpatterns = [
    # Django's built-in authentication URLs
    path('users/', include('django.contrib.auth.urls')),
    # Registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('users/logout/', views.logout_view, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),


    # password change URLs
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', MyPasswordChangeDoneView.as_view(), name='password_change_done'),
]
