from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import SubscribedUsers
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetView
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetDoneView

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')

def logout_view(request):
    """Log the user out."""
    logout(request)
    return redirect(reverse('shop:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process the completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect him to homepage.
            login(request, new_user)
            return redirect('shop:home')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, "Thank you for subscribing! " + f'{email}, You have successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))