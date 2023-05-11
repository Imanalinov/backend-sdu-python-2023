from django.urls import path

from . import views

urlpatterns = [
    path('', views.allPosts),
    path('post/create', views.createNewPost),
    path('post/<int:id>', views.postDetails),
    path('post/delete/<int:id>', views.deletePost),
    path('user/list', views.allUsers),
    path('user/create', views.createUser),
    path('user/<int:id>', views.userInfo),
    path('user/delete/<int:id>', views.deleteUser)
]
