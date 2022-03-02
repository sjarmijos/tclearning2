from re import T
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Widget

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(label='Nombre', required=True)
    last_name=forms.CharField(label='Apellido', required=True)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirma la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts={k:"" for k in fields}