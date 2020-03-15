from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
import json

# List all the currencies in JSON format
class CryptoView(ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request):
        for index in range(0,111):
            stock = get_object_or_404(Stock, id=index)

            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('name')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = percentChange[index]

            serializer = StockSerializer(instance=stock, data={'id': i, 'name': t, 'price': p, 'change': c, 'percentChange': pc}, many=False, partial=True)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleCryptoView(RetrieveUpdateDestroyAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer


# List all the stocks in JSON format
class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def put(self, request):
        for index in range(0,325):
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

            serializer = StockSerializer(instance=stock, data={'id': i, 'name': t, 'price': p, 'change': c, 'volume': v}, many=False, partial=True)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        for index in range(0,325):
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

            serializer = StockSerializer(data={'id': i, 'name': t, 'price': p, 'change': c, 'volume': v}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all the indices in JSON format
class IndiceList(APIView):
    def get(self, request):
        indices = Indice.objects.all()
        serializer = IndiceSerializer(indices, many=True)
        return Response(serializer.data)

    def put(self, request):
        for index in range(0,350):
            indice = get_object_or_404(Indice, id=index)

            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('name')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = percentChange[index]

            serializer = StockSerializer(instance=indice, data={'id': i, 'name': t, 'price': p, 'change': c, 'percentChange': pc}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        for index in range(0,35):
            id = request.data.getlist('id')
            i = id[index]
            ticker = request.data.getlist('name')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = float(percentChange[index])

            serializer = IndiceSerializer(data={'id': i, 'name': t, 'price': p, 'change': c, 'percentChange': pc}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all the Historical Data in JSON format
class MSFTView(APIView):
    def get(self, request):
        msft = MSFTHistorical.objects.all()
        serializer = MSFTSerializer(msft, many=True)
        return Response(serializer.data)

    def post(self, request):
        for index in range(0, 250):
            date = request.data.getlist('date')
            d = date[index]
            open = request.data.getlist('open')
            o = float(open[index])
            high = request.data.getlist('high')
            h = float(high[index])
            low = request.data.getlist('low')
            l = float(low[index])
            close = request.data.getlist('close')
            c = float(close[index])
            adjClose = request.data.getlist('adjClose')
            ac = float(adjClose[index])
            volume = request.data.getlist('volume')
            v = float(volume[index])

            serializer = MSFTSerializer(data={'date': d, 'open': o, 'high': h, 'low': l, 'close': c, 'adjClose': ac, 'volume': v}, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
