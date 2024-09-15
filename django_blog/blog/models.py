from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

# Create your models here.

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    
class Post(models.Model):
    title =  models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    author =
    content = 
    created_at = 
    updated_at = 
    