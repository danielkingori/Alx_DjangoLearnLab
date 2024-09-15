from django.urls import path
from .views import register,ListView,DetailView,CreateView,UpdateView,DeleteView, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", ListView, name="list_posts"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),  
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("post/new/", CreateView, name="create_post"),
    path("post/<int:pk>/read", DetailView, name="read_post"),
    path("post/<int:pk>/update/", UpdateView, name="edit_post"),
    path("post/<int:pk>/delete/", DeleteView, name ="delete_post"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
