import requests
from bs4 import BeautifulSoup

#For META
url = "https://www.cnbc.com/quotes/META"
url_request = requests.get(url)
html_request = BeautifulSoup(url_request.content, "html.parser")
search_data = html_request.find("div", class_="QuoteStrip-lastPriceStripContainer")
search_stock_price = search_data.find("span", class_="QuoteStrip-lastPrice")
print("The stock price for META is:", search_stock_price.text)

#For GOOGL
url = "https://www.cnbc.com/quotes/GOOGL"
url_request = requests.get(url)
html_request = BeautifulSoup(url_request.content, "html.parser")
search_data = html_request.find("div", class_="QuoteStrip-lastPriceStripContainer")
search_price = search_data.find("span")
print("The stock price for GOOGL is:", search_price.text)