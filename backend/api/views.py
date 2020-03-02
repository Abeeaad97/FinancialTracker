from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import StockSerializer
import json

# List all the stocks in JSON format
class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        for index in range(0,26):
            ticker = request.data.getlist('ticker')
            t = ticker[index]
            price = request.data.getlist('price')
            p = float(price[index])
            change = request.data.getlist('change')
            c = float(change[index])
            percentChange = request.data.getlist('percentChange')
            pc = float(percentChange[index])

            stock = Stock.objects.create(ticker=t,price=p,change=c,percentChange=pc)
            stock.save()

            serializer = StockSerializer(data=stock, many=False)
            if serializer.is_valid():
                serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
