from django.db import models
from django.contrib.auth.models import  AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50)
    confEmail = models.BooleanField(default=False)
    emailcode = models.CharField(max_length=6, default="")


    def __str__(self):
        return self.username

