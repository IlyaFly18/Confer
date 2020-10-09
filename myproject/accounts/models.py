from django.db import models
from django.contrib.auth.models import  AbstractUser
import django.contrib.auth.validators

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name="username")
    email = models.EmailField(unique=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=100, verbose_name="Email")
    confEmail = models.BooleanField(default=False)
    emailcode = models.CharField(max_length=6, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email