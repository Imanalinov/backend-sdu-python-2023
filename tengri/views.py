from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tengri.forms import SignIn, SignUp
from tengri.helper import passwordValidation, usernameValidation, emailValidation
from tengri.models import Post


def mainPage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'user': request.user
    }
    return render(request, 'pages/main.html', context)


def loginPage(request):
    error = None
    if request.method == 'POST':
        form = SignIn(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if form.is_valid() and user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Неправильный логин или пароль'

    else:
        error = None
        form = SignIn()

    return render(request, 'pages/login.html', {'form': form, 'error': error})


def SignUpPage(request):
    errors = {
        'password': None,
        'username': None,
        'email': None
    }
    if request.method == 'POST':
        form = SignUp(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        errors['password'] = passwordValidation(pass1, pass2)
        errors['username'] = usernameValidation(username)
        errors['email'] = emailValidation(email)
        if len(errors['password']) <= 0 and len(errors['username']) <= 0 and len(errors['email']) <= 0:
            user = User.objects.create_user(username, email, pass1)
            return HttpResponseRedirect('/login')

    else:
        form = SignIn()

    return render(request, 'pages/register.html', {'form': form, 'errors': errors})


def postPage(request, id):
    post = Post.objects.get(pk=id)
    post.watches = post.watches + 1
    post.save()
    context = {
        'post': post
    }
    return render(request, f'posts/{id}.html', context)


def custom_logout(request):
    logout(request)
    return redirect('/')


class PostAPIView(APIView):
    def delete(self, request, id, format=None):
        event = self.get_object(id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
