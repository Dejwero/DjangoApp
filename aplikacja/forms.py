from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    picture = forms.ImageField()
    class Meta:
        model = Post
        fields = ['picture', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']