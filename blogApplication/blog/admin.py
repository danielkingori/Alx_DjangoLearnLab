from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None,{"fields":("age",)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)

class CustomPostAdmin(admin.ModelAdmin):
    model = Post
    fields = ["title","author","content"]
    
admin.site.register(Post,CustomPostAdmin)