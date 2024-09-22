from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post



class CustomUserCreationForm(UserCreationForm):
    ROLES = [
        ("creator", "Creator"),
        ("reader", "Reader"),
    ]
    role = forms.ChoiceField(choices=ROLES, required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "email", "age", "role")