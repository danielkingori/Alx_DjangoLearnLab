from django.urls import path
from .views import index, list_books, LibraryDetailView, register, LoginView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('books', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register", register, name="register"),
    path("login", LoginView.as_view(next_page="product"), name="login"),
    # path("LogoutView", LogoutView.as_view(next_page="/"), name="logout"),
]