from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from tengri.models import Post


# Create your views here.
def createNewPost(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        file = request.FILES['file']
        imgUrl = request.POST.get('imgUrl')
        if title != None:
            post = Post.objects.create(title=title, html_url='empty', watches=0, time=datetime.now())
            save_path = '/Users/imanalinov/PycharmProjects/lab4/templates/posts/'
            with open(save_path + str(post.id) + ".html",
                      "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            post.html_url = str(post.id) + ".html"
            post.imgUrl = imgUrl
            post.save()
            return redirect('/adminka/')

    return render(request, 'admin/create-post.html')


def allPosts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'admin/all-posts.html', context)


def postDetails(request, id):
    post = Post.objects.get(pk=id)
    if (request.method == 'POST'):
        title = request.POST.get('title')
        fileUrl = request.POST.get('file')
        watch = request.POST.get('watch')

        post.html_url = fileUrl
        post.title = title
        post.watches = watch

        post.save()

    context = {
        'post': post
    }
    return render(request, 'admin/one-post.html', context)


def deletePost(request, id):
    if (id == None):
        return redirect('/adminka/')
    post = Post.objects.get(pk=id)
    if (post == None):
        return redirect('/adminka/')
    post.delete()
    return redirect('/adminka/')


def allUsers(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'admin/all-users.html', context)


def createUser(request):
    return render(request, 'admin/create-user.html')


def userInfo(request, id):
    user = User.objects.get(pk=id)
    if (request.method == 'POST'):
        # username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()
        return redirect('/adminka/user/list')

    context = {
        'user': user
    }
    return render(request, 'admin/user.html', context)


def deleteUser(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/adminka/user/list')
