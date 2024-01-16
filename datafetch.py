import requests


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