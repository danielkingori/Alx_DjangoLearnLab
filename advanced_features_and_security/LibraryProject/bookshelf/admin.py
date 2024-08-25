from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Book
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title', 'publication_year')
    model = Book
    
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


# class UserAdmin(CustomUserAdmin):
#     pass
admin.site.register(CustomUser, CustomUserAdmin)