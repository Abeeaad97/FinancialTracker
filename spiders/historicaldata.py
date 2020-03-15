import re
from io import StringIO
from datetime import datetime, timedelta
import requests
import pandas as pd

API_ENDPOINT = "http://localhost:8000/msft/"


class HistoricalData:
    timeout = 2
    crumb_link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    crumble_regex = r'CrumbStore":{"crumb":"(.*?)"}'
    quote_link = 'https://query1.finance.yahoo.com/v7/finance/download/{quote}?period1={dfrom}&period2={dto}&interval=1d&events=history&crumb={crumb}'

    def __init__(self, symbol, days_back=7):
        self.symbol = symbol
        self.session = requests.Session()
        self.dt = timedelta(days=days_back)

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
        return data


#pd.read_csv(StringIO(response.text), parse_dates=['Date'])

df = HistoricalData('MSFT', days_back=362).get_quote()

requests.post(url=API_ENDPOINT, data=df)


#df.to_csv(r'C:\Users\tyler\Documents\FinancialTracker\data.csv')
