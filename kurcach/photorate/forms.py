from django.forms import ModelForm, TextInput, ImageField, Select
from .models import photos
from django import forms

class CreatePhotoForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'id': "login", 'type': "text", 'class': "fadeIn second", 'name': "login", 'placeholder': "Название фото"
    }))
    author = forms.CharField(widget=forms.TextInput(attrs={
        'id': "login", 'type': "text", 'class': "fadeIn third", 'name': "login", 'placeholder': "Автор"
    }))
    class Meta:
        model = photos
        fields = ["title", "author", "photo"]
