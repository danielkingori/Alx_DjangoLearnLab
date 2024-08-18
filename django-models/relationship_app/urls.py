from django.urls import path
from .views import list_books, LibraryDetailView

from . import views

urlpatterns = [
    path('books', list_books, name='list_books'),
    path("", views.index, name="index"),
    path('library/<int:pk>/',LibraryDetailView.as_view(), name='library_detail'),
]