# comments/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Add a comment...'
        })
    )

    class Meta:
        model = Comment
        fields = ['text']
