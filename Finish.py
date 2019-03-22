import requests
from bs4 import BeautifulSoup
url = "https://coinyep.com/th/ex/THB-CAD"
url2 = "https://coinyep.com/th/ex/THB-KRW"
url3 = "https://coinyep.com/th/ex/THB-AUD"
url4 = "https://coinyep.com/th/ex/BRL-THB"
url5 = 'https://coinyep.com/th/ex/THB-CHF'
url6 = "https://coinyep.com/th/ex/THB-PLN"
c = requests.get(url)
c.encoding = 'utf-8'
soup = BeautifulSoup(c.text,'lxml')
Canada = soup.find_all(class_="container-fluid")
for i in Canada:
    print(i)
k = requests.get(url2)
k.encoding = 'utf-8'
soup2 = BeautifulSoup(k.text,'lxml')
Korea = soup2.find_all(class_="container-fluid")
for x in Korea:
    print(x)
a = requests.get(url3)
a.encoding = "utf-8"
page = BeautifulSoup(a.text,"lxml")
Australia = page.find_all(class_="container-fluid")
for t in Australia:
    print(t)
z = requests.get(url4)
z.encoding = "utf-8"
page2 = BeautifulSoup(z.text,"lxml")
Brazil = page2.find_all(class_="container-fluid")
for B in Brazil:
    print(B)
s = requests.get(url5)
s.encoding = 'utf-8'
soup3 = BeautifulSoup(s.text,'lxml')
Swit = soup3.find_all(class_="container-fluid")
for w in Swit:
    print(w)
p = requests.get(url6)
p.encoding = 'utf-8'
page3 = BeautifulSoup(p.text,'lxml')
Poland = page3.find_all(class_="container-fluid")
for l in Poland:
    print(l)