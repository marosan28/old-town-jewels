from django import forms
from tinymce.widgets import TinyMCE
from .models import Review
from users.models import Profile


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].required = True

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not rating:
            raise forms.ValidationError("Please select a rating")
        return rating
