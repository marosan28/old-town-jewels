from django import forms
from tinymce.widgets import TinyMCE
from .models import Review
from users.models import Profile


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

class ReviewForm(forms.ModelForm):
    profile = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput())

    class Meta:
        model = Review
        fields = ['profile', 'body', 'rating']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.HiddenInput(),
        }
        labels = {
            'body': 'Review',
            'rating': 'Rating',
        }
        help_texts = {
            'body': 'Write your review',
            'rating': 'Select a rating',
        }
        error_messages = {
            'body': {
                'required': 'Please write your review',
            },
            'rating': {
                'required': 'Please select a rating',
            }
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        queryset = Profile.objects.filter(user=user)
        super().__init__(*args, **kwargs)
        self.fields['profile'].queryset = queryset

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not rating:
            raise forms.ValidationError("Please select a rating")
        return rating
