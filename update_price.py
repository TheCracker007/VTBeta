# update_price.py

import requests
from bs4 import BeautifulSoup

def get_sell_price():
    url = 'https://www.binance.com/en/orderbook/USDT_VAI'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the sell price is in the first row of the sell orders
        sell_price = float(soup.select('.showPrice')[0].text.strip())
        return sell_price
    else:
        return None

def update_readme(price):
    with open('readme.md', 'w') as readme_file:
        if price >= 1.002:
            readme_file.write(f"Price not reached, current price is {price} VAI/USDT")
        else:
            readme_file.write(f"Price reached, current price is {price} VAI/USDT")

if __name__ == "__main__":
    sell_price = get_sell_price()

    if sell_price is not None:
        update_readme(sell_price)
