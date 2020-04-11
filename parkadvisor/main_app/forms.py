# delete this file if go with CBVs
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'category', 'comments', 'image', 'park_rating', 'likes']

