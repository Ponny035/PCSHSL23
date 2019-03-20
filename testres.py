import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.bot.or.th/Thai/FinancialMarkets/MonetaryOperations/_layouts/Application/ExchangeRate/ExchangeRate.aspx'
r = requests.get(url)
r.encoding = 'utf-8'
page = BeautifulSoup(r.text,'lxml')
pageTitle = page.td.find_all(class_="tx-news")
pattern = "(?:[0-9]+(\.)*|\.)([0-9])*E*(?:\+([0-9])*|\-([0-9])*)*"
for x in pageTitle:
    print(x)
