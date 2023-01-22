from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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
            return redirect('shop:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)