from django import forms

from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':60, 'style':'font-size: larger; color: grey; font-weight: bolder;'})}