from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Form_comida(forms.Form):
    nombre = forms.CharField(max_length=20)
    desc = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

