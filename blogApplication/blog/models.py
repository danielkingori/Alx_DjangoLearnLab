from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

# Create your models here.
# class CustomUser(AbstractUser):
#     age = models.IntegerField(blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

#creating a Post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content =  models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        permissions = [
        ("create", "Can create posts"),
        ("read", "Can read posts"),
        ("edit", "Can edit posts"),
        # ("delete", "Can edit posts"),
    ]