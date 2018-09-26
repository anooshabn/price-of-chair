__author__ = 'anushabn'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip() #£129.00

price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 200:
    print("You should buy the chair!")
    print("The current price is {}".format(string_price))
elif price == 200:
    print("Buy it if you really want to!")
else:
    print("Don't buy the chair, it's too expensive!")





# https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183
# <p class="price price--large">£129.00 </p>
