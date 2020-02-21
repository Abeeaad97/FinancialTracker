from django.db import models

# Template Model
class Stock(models.Model):
    ticker = models.CharField(max_length=10)           # Name of the stock
    open = models.FloatField()                         # Opening stock price
    close = models.FloatField()                        # Closing stock price
    volume = models.IntegerField()                     # Amount of sales

    def __str__(self):
        return self.ticker

