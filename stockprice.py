import requests
from bs4 import BeautifulSoup
url = "https://www.cnbc.com/quotes/META"
url_request = requests.get(url)
html_request = BeautifulSoup(url_request.content, "html.parser")
search_data = html_request.find("div", class_="QuoteStrip-lastPriceStripContainer")
search_stock_price = search_data.find("span", class_="QuoteStrip-lastPrice")
print(search_stock_price.text)