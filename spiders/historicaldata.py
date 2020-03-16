import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
from datetime import datetime, timedelta
import requests
import json
import pandas as pd
import re

API_ENDPOINT = "http://localhost:8000/msft/"


class HistoricalData:
    timeout = 2
    crumb_link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    crumble_regex = r'CrumbStore":{"crumb":"(.*?)"}'
    quote_link = 'https://query1.finance.yahoo.com/v7/finance/download/{quote}?period1={dfrom}&period2={dto}&interval=1d&events=history&crumb={crumb}'

    def __init__(self, quote, days):
        self.symbol = quote
        self.session = requests.Session()
        self.dt = timedelta(days=days)

        self.quote = quote
        self.days = days

    def get_crumb(self):
        response = self.session.get(self.crumb_link.format(self.symbol), timeout=self.timeout)
        response.raise_for_status()
        match = re.search(self.crumble_regex, response.text)
        if not match:
            raise ValueError('Could not get crumb from Yahoo Finance')
        else:
            self.crumb = match.group(1)

    def get_quote(self):
        if not hasattr(self, 'crumb') or len(self.session.cookies) == 0:
            self.get_crumb()
        now = datetime.utcnow()
        dateto = int(now.timestamp())
        datefrom = int((now - self.dt).timestamp())
        url = self.quote_link.format(quote=self.symbol, dfrom=datefrom, dto=dateto, crumb=self.crumb)
        response = self.session.get(url)
        response.raise_for_status()
        test = response.text.replace('\n', '').split(",")

        data = {
            "date": [],
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "adjClose": [],
            "volume": []
        }

        for index in range (6, 1506, 6):
            currentData = test[index]
            if index == 6:
                data["date"].append(currentData[6:])
            elif index == 1500:
                data["volume"].append(currentData[:8])
                data["volume"].append(test[index+6])
                data["date"].append(currentData[8:])
            else:
                data["volume"].append(currentData[:8])
                data["date"].append(currentData[8:])
            data["open"].append(test[index+1])
            data["high"].append(test[index+2])
            data["low"].append(test[index+3])
            data["close"].append(test[index+4])
            data["adjClose"].append(test[index+5])

        print(data["date"])
        #pd.read_csv(StringIO(response.text), parse_dates=['Date'])
        return data


    def create_candlestick(self):
        r = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{self.quote}?timeseries={self.days}')
        r = r.json()

        stockdata = r['historical']
        stockdata_df = pd.DataFrame(stockdata)

        fig = go.Figure(data=[go.Candlestick(x=stockdata_df['date'],
                        open=stockdata_df['open'],
                        high=stockdata_df['high'],
                        low=stockdata_df['low'],
                        close=stockdata_df['close'])])
        fig.update_layout(
            title= {
                'text': self.quote,
              'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
              font=dict(
                family="Courier New, monospace",
                size=20,
                color="#7f7f7f"
            )
            )

        fig.show()


HistoricalData('MSFT', days=365).create_candlestick()


#MSFT = HistoricalData('MSFT', days=365).get_quote()
#requests.post(url=API_ENDPOINT, data=MSFT)
