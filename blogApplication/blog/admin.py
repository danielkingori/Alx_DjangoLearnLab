from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post
# Register your models here.

# admin.site.unregister(User)
# class User(UserAdmin):
#     model = User
#     fieldsets = UserAdmin.fieldsets + (
#         (None,{"fields":("age",)}),
#     )
# admin.site.register(User, UserAdmin)

class CustomPostAdmin(admin.ModelAdmin):
    model = Post
    fields = ["title","author","content"]
    
admin.site.register(Post,CustomPostAdmin)