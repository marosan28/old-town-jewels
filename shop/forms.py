from django import forms
from tinymce.widgets import TinyMCE
from .models import Review

class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

class ReviewForm(forms.ModelForm):
    
    name = forms.CharField(label='Name', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Review', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Review
        fields = ('name', 'email', 'body')


