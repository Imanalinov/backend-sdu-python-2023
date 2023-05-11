from django import template
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

register = template.Library()


def passwordValidation(pass1, pass2):
    err = []
    if pass1 != pass2:
        err.append('Пароли не совпадают')
    if len(pass1) < 6 and len(pass2) > 20:
        err.append('Неправильный формат пароля')
    return err


def usernameValidation(username):
    err = []
    users = get_user_model().objects.all()
    for user in users:
        print(user.username)
        if username == user.username:
            err.append('Пользователь уже существует')

    return err


def emailValidation(email):
    err = []
    try:
        validate_email(email)
    except ValidationError as e:
        err.append("неверная почта")

    users = get_user_model().objects.all()
    for user in users:
        print(user.username)
        if email == user.email:
            err.append('Email уже существует')

    return err


@register.filter
def hash(d, key):
    return d[key]
