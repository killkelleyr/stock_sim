from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    balance = models.FloatField(default=0.0)

class Position(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    qantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT) #FK link

    def __str__(self):
        return self.symbol

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    actionType = models.CharField(max_length=4, choices=(('BUY','Buy'),('SELL','Sell'),)) # buy/sell
    quantity = models.IntegerField()
    symbol = models.CharField(max_length=10)
    actionPrice = models.FloatField(default=0.0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT) #FK link to portfolio