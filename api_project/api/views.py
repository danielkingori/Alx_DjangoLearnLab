from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.generic.ListAPIViews import ListAPIView

# Create your views here.


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer