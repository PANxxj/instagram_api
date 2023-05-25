from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    username=models.CharField(unique=True,max_length=16)
    boi=models.CharField(max_length=100)

    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User,models.SET_NULL,null=True,related_name='user_post')
    
    
class PostLikes(models.Model):
    post = models.ForeignKey(Post,models.CASCADE,null=False)
    user=models.ForeignKey(User,models.CASCADE,null=False)
    
    class Meta:
        unique_together =(('post', 'user'),)