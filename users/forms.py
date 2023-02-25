from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
from cloudinary.compat import to_bytes
import cloudinary
import hashlib
from django.conf import settings


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


User = get_user_model()


class UserWidget(forms.widgets.HiddenInput):
    def render(self, name, value, attrs=None, renderer=None):
        return super().render(name, value.id if value else None, attrs, renderer)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'date_of_birth']

    user = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=UserWidget)
