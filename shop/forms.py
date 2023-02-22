from django import forms
from tinymce.widgets import TinyMCE
from .models import Review

class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'body', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.HiddenInput(),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'body': 'Review',
            'rating': 'Rating',
        }
        help_texts = {
            'name': 'Enter your name',
            'email': 'Enter your email',
            'body': 'Write your review',
            'rating': 'Select a rating',
        }
        error_messages = {
            'name': {
                'required': 'Please enter your name',
            },
            'email': {
                'required': 'Please enter your email address',
                'invalid': 'Please enter a valid email address',
            },
            'body': {
                'required': 'Please write your review',
            },
            'rating': {
                'required': 'Please select a rating',
            }
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not rating:
            raise forms.ValidationError("Please select a rating")
        return rating



