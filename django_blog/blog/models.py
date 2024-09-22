from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings 
from taggit.managers import TaggableManager

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title =  models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ManyToManyField(Post, related_name='posts')
    def _str_(self):
        return self.name
    