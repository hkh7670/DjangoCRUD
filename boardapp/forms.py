from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "body",)
        labels = {
            'title': '제목',
            'body': '내용',
        }

class SearchForm(forms.ModelForm):
    class Meta:
        title = forms.CharField(label='title')