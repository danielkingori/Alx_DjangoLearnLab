from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    
    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete_books", "Can delete books"), 
        ]

    def __str__(self):
        return self.title

class BookList(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    books =  models.ManyToManyField(Book, related_name="book_lists")
    
    class Meta:
        permissions = [
            ("can_view_booklists", "Can view books lists"),
            ("can_create_booklists", "Can create book lists"),
            ("can_edit_booklists", "Can edit book lists"),
            ("can_delete_booklists", "Can delete book lists"),
        ]
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
    
    
