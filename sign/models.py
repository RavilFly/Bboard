from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.db import models


# class BaseRegisterForm(UserCreationForm):
#     email = forms.EmailField(label = "Email")
#
#     class Meta:
#         model = User
#         fields = ("username",
#                   "email",
#                   "password1",
#                   "password2", )

class OneTimeCode(models.Model):
    user = models.CharField(max_length=256)
    code = models.CharField(max_length=10)