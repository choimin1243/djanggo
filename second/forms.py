# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content']

        labels={
            'title': _('제목'),
            'content': _('내용'),
        }
