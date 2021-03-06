from django.db import models

# Template Model
class Crypto(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100)           # Name of the stock
    price = models.CharField(max_length=20)                         # Opening stock price
    change = models.CharField(max_length=20)                        # Closing stock price
    percentChange = models.CharField(max_length=20)                     # Amount of sales

    def __str__(self):
        return self.name


class Stock(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100)           # Name of the stock
    price = models.CharField(max_length=20)                         # Opening stock price
    change = models.CharField(max_length=20)                        # Closing stock price
    volume = models.CharField(max_length=20)            # Amount of sales

    def __str__(self):
        return self.name


class Indice(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100)           # Name of the stock
    price = models.CharField(max_length=20)                         # Opening stock price
    change = models.CharField(max_length=20)                        # Closing stock price
    percentChange = models.CharField(max_length=20)            # Amount of sales

    def __str__(self):
        return self.name


class MSFTHistorical(models.Model):
    date = models.CharField(primary_key=True, max_length=10, default="")
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    adjClose = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.date
