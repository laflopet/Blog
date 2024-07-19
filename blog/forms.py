from django import forms
from .models import Post


class BlogCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')