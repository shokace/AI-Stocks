import datafetch
import dataplot
import logging
import time
import os


while True:
    try:
        tm_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&x_cg_demo_api_key={}"
        coingecko_token = os.getenv('COINGECKO_KEY')
        url = tm_url.format(coingecko_token)
        # Fetch data        
        crypto_data = datafetch.fetch_crypto_data(url)
        top_crypto = datafetch.top_mover(crypto_data)
        logging.info("Top crypto: %s", top_crypto)
    except Exception as e:
        logging.error("Base data could not be fetched: %s", e)

    if crypto_data:
        if top_crypto:
            crypto_name = top_crypto['id']
            granular_data = datafetch.fetch_granular_data(crypto_name)
            dataplot.plotdata(crypto_name, granular_data)
            logging.info("GRAPH UPDATED")
        else:
            logging.info("No top mover found.")
    else:
        logging.error("Failed to fetch data.")

    time.sleep(301)  # Wait for 5 min and 1 sec. Graph shows up in 5 min intervals anyways.


        