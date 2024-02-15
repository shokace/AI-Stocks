from flask import Flask, render_template
from dotenv import load_dotenv
import threading
import time
import datetime as datetime
import datafetch
import dataplot
import os
import logging

load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("This is an info message")

def periodic_fetch():
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

@app.route('/')
def index():
    file_path = 'backupStorage/backupGraph.html'
    with open(file_path, 'r') as file:
        defaultFig = file.read()

    return render_template('index.html', graph_html=defaultFig)

if __name__ == "__main__":
    logging.info("This is an info message in __main__")
    t = threading.Thread(target=periodic_fetch)
    t.daemon = True  # This makes the thread terminate when the main program exits
    t.start()  # Start the thread
    app.run(debug=False, host="127.0.0.1", port=8000)
