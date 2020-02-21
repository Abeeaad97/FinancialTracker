from rest_framework import serializers
from .models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('ticker', 'volume')
