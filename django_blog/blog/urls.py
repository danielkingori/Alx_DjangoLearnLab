from django.urls import path
from .views import register,ListView,DetailView,CreateView,UpdateView,DeleteView, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", ListView, name="list_posts"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),  
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("create_post", CreateView, name="create_post"),
    path("read_post", DetailView, name="read_post"),
    path("edit_post/<int:pk>", UpdateView, name="edit_post"),
    path("delete_post/<int:pk>", DeleteView, name ="delete_post"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]