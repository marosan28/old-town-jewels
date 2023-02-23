from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import SubscribedUsers, Profile
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetView
from django.contrib.auth import logout
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from .forms import Login, UserRegistrationForm, UserEditForm, ProfileEditForm
import cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary import api


# Password Reset 
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')

# Password Change
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
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
             # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user

            # Check if the image file is uploaded
            if 'image' in request.FILES:
                # Upload the image file to Cloudinary
                response = cloudinary.uploader.upload(request.FILES['image'], folder="profiles/")

                # Set the image url in the profile model
                profile.image = response['secure_url']

            profile.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('users:edit')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})



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


# Edit profile 

