from pagedown.widgets import AdminPagedownWidget
from django import forms
from models import Post


class PostModelForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
