from django.urls import path
from .views import index, list_books, LibraryDetailView, register, LoginView, LogoutView, add_book, edit_book, delete_book
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('books', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("LogoutView", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('books/add/<int:pk>/', add_book/, name='add_book'),
    path('books/edit/<int:pk>/', edit_book/, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]