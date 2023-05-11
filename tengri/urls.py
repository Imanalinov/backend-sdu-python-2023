from django.urls import path

from . import views
from .views import PostAPIView

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('post/<int:id>', views.postPage, name='post'),
    path('login', views.loginPage, name='login'),
    path('register', views.SignUpPage, name='sign_up'),
    path(r'^v1/post/\d+', PostAPIView.as_view()),
    path('logout', views.custom_logout)
]
