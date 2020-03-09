import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests

API_ENDPOINT = "http://localhost:8000/indices/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"

# Data Table
names=[]
prices=[]
changes=[]
percentChanges=[]

# URL to scrape data from
IndicesUrl = "https://finance.yahoo.com/world-indices"

# Send a GET request to retrieve html
r = requests.get(IndicesUrl)
data = r.text

# Load the data into soup
soup = BeautifulSoup(data, 'lxml')

for name in soup.find_all('td', attrs={'class':'data-col1'}):
    names.append(name.text)
for price in soup.find_all('td', attrs={'class':'data-col2'}):
    prices.append(float(price.text.replace(',', '')))
for change in soup.find_all('td', attrs={'class':'data-col3'}):
    changes.append(float(change.text.replace(',', '')))
for percentChange in soup.find_all('td', attrs={'class':'data-col4'}):
    percentChanges.append(float(percentChange.text.replace(',', '').replace('%', '')))

data = {
    "ticker": names,
    "price": prices,
    "change": changes,
    "percentChange": percentChanges
}

requests.post(url=API_ENDPOINT, data={"ticker": data["ticker"], "price": data["price"], "change": data["change"], "percentChange": data["percentChange"]})
