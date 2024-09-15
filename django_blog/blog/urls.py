from django.urls import path
from .views import register,create_post,edit_post,list_posts,delete_post, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", list_posts, name="list_posts"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),  
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("create_post", create_post, name="create_post"),
    path("edit_post/<int:pk>", edit_post, name="edit_post"),
    path("delete_post/<int:pk>", delete_post, name ="delete_post"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]