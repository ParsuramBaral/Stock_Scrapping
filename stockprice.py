import requests
from bs4 import BeautifulSoup

#For META
company_list = ["META","TSLA","GOOGL","KO","AMZN","AAPL","NVDA","MSFT","NVR","BRK.A"]
for i in company_list:
    url="https://www.cnbc.com/quotes/" + i
    url_request = requests.get(url)
    html_request = BeautifulSoup(url_request.content, "html.parser")
    search_data = html_request.find("div", class_="QuoteStrip-lastPriceStripContainer")
    search_stock_price = search_data.find("span", class_="QuoteStrip-lastPrice")
    print("\nThe stock price for ",i ,"is", search_stock_price.text)


