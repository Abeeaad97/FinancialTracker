import requests from bs4
import BeautifulSoup
import csv
import pandas as pd

names=[]
prices=[]
changes=[]
precentChangess=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

for index in range(0,10):
    CryptoCurrencies = "https://in.finance.yahoo.com/cryptocurrencies?offset="
    + str(index) + "&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=50"

    r = requests.get(CryptoCurrencies)
    data = r.text
    soup = BeautifulSoup(data)

    for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Price (intraday)'}):
            prices.append(price.find('span').text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'aria-label': '% Change'}):
            percentChanges.append(percentChange.text)
        for marketCap in listing.find_all('td', attrs={'aria-label': 'Market Cap'}):
            marketCaps.append(marketCap.text)
        for totalVolume in listing.find_all('td', attrs={'aria-label': 'Total Volume (24 hrs)'}):
            totalVolumes.append(totalVolume.text)
        for circulatingSupply in listing.find_all('td', attrs={'aria-label': 'Circulating Supply'}):
            circulatingSupplys.append(circulatingSupply.text)
