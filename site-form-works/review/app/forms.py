from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, max_length=2000, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
