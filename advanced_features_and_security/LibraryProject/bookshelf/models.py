from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission

# Create your models here.

#Get the Permission
permission = Permission.objects.get(codename='add_post')

#Assign permission to a user
user.user_permission.add(permission)

#Assign permisson to a group
group.permissions.add(permission)


# class UserManager(BaseUserManager):
#     def create_user(self, email, password):
#         if not email:
#             raise ValueError("User must provide an email")
#         user = self.model(email = self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
        
class Permission:
    def __init__(self, can_view=False, can_create=False, can_edit=False, can_delete=False):
        self.can_view = can_view
        self.can_edit = can_edit
        self.can_create = can_create
        self.can_delete = can_delete
class Role:
    def __init__(self) -> None:
        pass
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
        

    def __str__(self):
        return self.title
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, date_of_birth, password, **extra_fields)
   

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255, verbose_name='EmailAddress')
    username = models.CharField(unique=False, max_length=25)
    # bio = models.TextField(blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    
    
