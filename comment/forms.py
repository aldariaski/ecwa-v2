from django import forms
from .models import *

class FormPost(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {"placeholder" : "Title, max 50 characters", 'class': 'form-control my-1'}), label = "")
    content = forms.CharField(max_length=1500, widget=forms.Textarea(attrs = {"placeholder" : "Content, max 1500 characters", 'class': 'form-control my-1', 'rows':'3'}), label = "")
    class Meta:
        model = Post
        exclude = ["user"]

class FormComment(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea(attrs = {"placeholder" : "Insert Comment Here, max 500 characters", 'class': 'form-control', 'rows':'3'}), label = "")
    class Meta:
        model = Comment
        exclude = ["user","post", "deleted"]