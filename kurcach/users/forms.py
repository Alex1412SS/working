from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import MyUser
from django import forms


class UserRegistrationForm(UserCreationForm):
    username_real = forms.CharField(widget=forms.TextInput(attrs={
        'id': "login", 'type': "text",'class':"fadeIn second", 'name': "login", 'placeholder': "Имя"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "login", 'type': "text",'class':"fadeIn second", 'name': "login", 'placeholder': "Логин"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "password", 'type': "text",'class': "fadeIn third", 'name': "login",'placeholder': "Пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "password", 'type': "text",'class': "fadeIn third", 'name': "login",'placeholder': "Подтвердите пароль"
    }))

    class Meta:

        model = MyUser
        fields = ("username_real", "username", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "login", 'type': "text",'class':"fadeIn second", 'name': "login", 'placeholder': "Логин"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "password", 'type': "text",'class': "fadeIn third", 'name': "login", 'placeholder': "Пароль"
    }))

    class Meta:

        model = MyUser
        fields = ("username", "password")


class UserProfile(UserChangeForm):
    username_real = forms.CharField(widget=forms.TextInput)
    user_name = forms.CharField(widget=forms.TextInput)
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = MyUser
        fields = ("username_real", "user_name", "image")
