from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    