from rest_framework import serializers
from .models import *

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('id', 'ticker', 'price', 'change', 'percentChange')

    def update(self, instance, validated_data):
        instance.ticker = validated_data.get('ticker', instance.ticker)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.volume = validated_data.get('percentChange', instance.volume)

        instance.save()
        return instance


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'ticker', 'price', 'change', 'volume')

    def update(self, instance, validated_data):
        instance.ticker = validated_data.get('ticker', instance.ticker)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.volume = validated_data.get('volume', instance.volume)

        instance.save()
        return instance


class IndiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indice
        fields = ('id', 'ticker', 'price', 'change', 'percentChange')

    def update(self, instance, validated_data):
        instance.ticker = validated_data.get('ticker', instance.ticker)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.volume = validated_data.get('percentChange', instance.volume)

        instance.save()
        return instance
