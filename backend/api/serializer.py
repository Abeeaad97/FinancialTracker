from rest_framework import serializers
from .models import *

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('id', 'name', 'price', 'change', 'percentChange')

    def create(self, validated_data):
        return Crypto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.percentChange = validated_data.get('percentChange', instance.percentChange)

        instance.save()
        return instance


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'name', 'price', 'change', 'volume')

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.volume = validated_data.get('volume', instance.volume)

        instance.save()
        return instance


class IndiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indice
        fields = ('id', 'name', 'price', 'change', 'percentChange')

    def create(self, validated_data):
        return Indice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.change = validated_data.get('change', instance.change)
        instance.percentChange = validated_data.get('percentChange', instance.percentChange)

        instance.save()
        return instance


class MSFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSFTHistorical
        fields = ('date', 'open', 'high', 'low', 'close', 'adjClose', 'volume')

    def create(self, validated_data):
        return MSFTHistorical.objects.create(**validated_data)
