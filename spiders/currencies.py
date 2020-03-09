import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests

API_ENDPOINT = "http://localhost:8000/currencies/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"

# Data Table
names=[]
prices=[]
changes=[]
percentChanges=[]

# URL to scrape data from
CurrenciesUrl = "https://finance.yahoo.com/currencies"

# Send a GET request to retrieve html
r = requests.get(CurrenciesUrl)
data = r.text

# Load the data into soup
soup = BeautifulSoup(data, 'lxml')

# For Loop - Yahoo Finance requires us to crawl through data-id attributes
# the range was determined by their specific pattern of id increments
for index in range(40, 404, 14):
    # For Loop - grab each listing row and extract the data individually
    for listing in soup.find_all('tr', attrs={'data-reactid':index}):
        for name in listing.find_all('td', attrs={'data-reactid':index+3}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'data-reactid':index+4}):
            prices.append(float(price.text.replace(',', '')))
        for change in listing.find_all('td', attrs={'data-reactid':index+5}):
            changes.append(float(change.text.replace(',', '')))
        for percentChange in listing.find_all('td', attrs={'data-reactid':index+7}):
            percentChanges.append(float(percentChange.text.replace(',', '').replace('%', '')))

data = {
    "ticker": names,
    "price": prices,
    "change": changes,
    "percentChange": percentChanges
}

requests.post(url=API_ENDPOINT, data={"ticker": data["ticker"], "price": data["price"], "change": data["change"], "percentChange": data["percentChange"]})
