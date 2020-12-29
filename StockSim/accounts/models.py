from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rhoodID = encrypt(models.CharField(max_length=50))
    rhoodPWD = encrypt(models.CharField(max_length=50))
    rhQ = encrypt(models.CharField(max_length=50))
