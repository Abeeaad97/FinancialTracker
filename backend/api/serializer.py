from rest_framework import serializers
from .models import *

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('id', 'ticker', 'price', 'change', 'percentChange')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'ticker', 'price', 'change', 'volume')


class IndiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indice
        fields = ('ticker', 'price', 'change', 'percentChange')
