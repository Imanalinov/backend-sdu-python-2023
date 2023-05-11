from django import forms
from django.contrib.auth.models import User


class SignIn(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignUp(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        # fields = ("username", "email", "password1", "password2")
        fields = "username"
