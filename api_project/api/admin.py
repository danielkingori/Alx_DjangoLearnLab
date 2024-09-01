from django.contrib import admin
from .models import Book
from rest_framework.authtoken.models import Token


# Register your models here.
admin.site.register(Token)
admin.site.register(Book)