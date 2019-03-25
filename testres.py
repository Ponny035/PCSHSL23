import requests
import re
from bs4 import BeautifulSoup
url = "https://coinyep.com/th/ex/THB-CAD"
url2 = "https://coinyep.com/th/ex/THB-KRW"
url3 = "https://coinyep.com/th/ex/THB-AUD"
url4 = "https://coinyep.com/th/ex/BRL-THB"
url5 = 'https://coinyep.com/th/ex/THB-CHF'
url6 = "https://coinyep.com/th/ex/THB-PLN"

pattern = "(?:coinyep-reverse[0-9]{1})" # Regular expressions
moneyId = re.compile(pattern)
c = requests.get(url)
c.encoding = 'utf-8'
soup = BeautifulSoup(c.text,'lxml')
Canada = soup.find_all(class_="row justify-content-md-center")
find = moneyId.findall(str(Canada))
f= open("index.txt","a+")
for i in find:
    Canada= soup.find(id=i)
    f.write(str(Canada)+"\n")
f.close()

# ทำต่อออออออออ
# c = requests.get(url2)
# c.encoding = 'utf-8'
# soup = BeautifulSoup(c.text,'lxml')
# Korea
