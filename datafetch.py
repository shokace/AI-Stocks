from dotenv import load_dotenv

import requests
import time
import os




current_unix_time = int(time.time())
#print("Current time: UNIX#", current_unix_time)
yesterday_unix_time = current_unix_time - 86400
load_dotenv()

def fetch_granular_data(crypto_name):
    base_url = "https://api.coingecko.com/api/v3/coins/{}/market_chart/range?vs_currency=usd&from={}&to={}&precision=8&x_cg_demo_api_key={}"   
    coingecko_token = os.getenv('COINGECKO_KEY')
    url = base_url.format(crypto_name, yesterday_unix_time, current_unix_time, coingecko_token)
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        print("COINGECKO API = 200")
        return response.json()
    else:
        # Handle errors (e.g., invalid cryptocurrency name, network issues)
        return None



def fetch_crypto_data(tm_url):
    
    response = requests.get(tm_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def top_mover(crypto_data):
    
    max_change = 0
    top_crypto = None
    for crypto in crypto_data:
        price_change_percentage_24h = crypto.get('price_change_percentage_24h', 0)
        if price_change_percentage_24h > max_change:
            max_change = price_change_percentage_24h
            top_crypto = crypto
    return top_crypto

