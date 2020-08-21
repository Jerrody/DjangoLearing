from django import forms

from .models import FeedBackForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBackForm
        fields = ('text',)
