import requests
from bs4 import BeautifulSoup
import time
from telegram.ext import Updater

# Telegram API key
TELEGRAM_API_KEY = 'TELEGRAM_API_KEY'

# Target URL
URL = 'https://www.nike.com/tr/t/blazer-mid-77-premium-ayakkab%C4%B1s%C4%B1-LRWMKw/DQ7672-100'

# Prive
ISTEDIGINIZ_FIYAT = 100  

# Telegram group ID
GRUP_ID = 'xxxxxx'

def check_price():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_element = soup.find('span', class_='product-price')
    if price_element is not None:
        price = float(price_element.get_text().replace(',', '.'))  

        if price <= ISTEDIGINIZ_FIYAT:
            updater = Updater(TELEGRAM_API_KEY)
            updater.bot.send_message(chat_id=GRUP_ID, text=f'Price is down.Come on !! {price} TL')
            updater.stop()

# BTimer
while True:
    check_price()
    time.sleep(3600)  # 1 hour
