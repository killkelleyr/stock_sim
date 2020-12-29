from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rhoodID = encrypt(models.CharField(max_length=50))
    rhoodPWD = encrypt(models.CharField(max_length=50))
    rhQ = encrypt(models.CharField(max_length=50))

def create_account(sender, **kwargs):
    userName = kwargs["instance"]
    if kwargs["created"]:
        account = Account(user=userName)
        account.save()

post_save.connect(create_account, sender=User)