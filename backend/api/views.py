from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
import json

# List all the currencies in JSON format
class CryptoList(APIView):
    def get(self, request):
        crypto = Crypto.objects.all()
        serializer = CryptoSerializer(crypto, many=True)
        return Response(serializer.data)

    def put(self, request):
        for index in range(0,111):
            stock = get_object_or_404(Stock, id=index)

            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = percentChange[index]

            serializer = StockSerializer(instance=stock, data={'id': i, 'ticker': t, 'price': p, 'change': c, 'percentChange': pc}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        for index in range(0,111):
            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = float(percentChange[index])

            crypto = Crypto.objects.create(id=i, ticker=t,price=p,change=c,percentChange=pc)
            crypto.save()

            serializer = CryptoSerializer(data=crypto, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all the stocks in JSON format
class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def put(self, request):
        for index in range(0,350):
            stock = get_object_or_404(Stock, id=index)

            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            volume = request.data.getlist('volume')
            v = volume[index]

            serializer = StockSerializer(instance=stock, data={'id': i, 'ticker': t, 'price': p, 'change': c, 'volume': v}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        for index in range(0,350):
            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            volume = request.data.getlist('volume')
            v = volume[index]

            stock = Stock.objects.create(id=i, ticker=t,price=p,change=c,volume=v)
            stock.save()

            serializer = StockSerializer(data=stock, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all the indices in JSON format
class IndiceList(APIView):
    def get(self, request):
        indices = Indice.objects.all()
        serializer = IndiceSerializer(indices, many=True)
        return Response(serializer.data)

    def post(self, request):
        for index in range(0,35):
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = float(percentChange[index])

            indice = Indice.objects.create(ticker=t,price=p,change=c,percentChange=pc)
            indice.save()

            serializer = IndiceSerializer(data=indice, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
