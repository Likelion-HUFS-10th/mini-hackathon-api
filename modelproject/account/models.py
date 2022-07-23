from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=100, null=True)
