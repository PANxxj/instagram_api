from django.urls import path

from .user import *
from .post import *

urlpatterns = [
    path('user/create', CreateUser.as_view()),
    path('user/login', UserLogin.as_view()),
    path('user/<int:pk>',RetriveUser.as_view()),
    path('user/update', UpdateUser.as_view()),
    path('user/delete', DeleteUser.as_view()),
    
    
    path('post/create', CreatePost.as_view()),
    path('post/<int:pk>', RetrivePost.as_view()),
    path('post/update/<int:pk>', UpdatePost.as_view()),
    path('post/delete/<int:pk>', DeletePost.as_view()),
    path('post/list',View.as_view()),
    path('post/like/<int:pk>',LikePost.as_view()),
]
