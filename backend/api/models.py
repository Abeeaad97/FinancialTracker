from django.db import models

# Template Model
class Currency(models.Model):
    ticker = models.CharField(max_length=10)           # Name of the stock
    price = models.FloatField()                         # Opening stock price
    change = models.FloatField()                        # Closing stock price
    percentChange = models.FloatField()                     # Amount of sales

    def __str__(self):
        return self.ticker


class Stock(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    ticker = models.CharField(max_length=10)           # Name of the stock
    price = models.FloatField()                         # Opening stock price
    change = models.FloatField()                        # Closing stock price
    volume = models.CharField(max_length=10)            # Amount of sales

    def __str__(self):
        return self.ticker


class Indice(models.Model):
    ticker = models.CharField(max_length=10)           # Name of the stock
    price = models.FloatField()                         # Opening stock price
    change = models.FloatField()                        # Closing stock price
    percentChange = models.FloatField()            # Amount of sales

    def __str__(self):
        return self.ticker
