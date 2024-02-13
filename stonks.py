from flask import Flask, render_template
from dotenv import load_dotenv


import threading
import time
import datetime as datetime
import datafetch
import dataplot
import os

load_dotenv()



app = Flask(__name__)

def periodic_fetch():
    while True:
        
        tm_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&x_cg_demo_api_key={}"
        coingecko_token = os.getenv('COINGECKO_KEY')
        url = tm_url.format(coingecko_token)
        # Fetch data        
        try:
            crypto_data = datafetch.fetch_crypto_data(url)
            top_crypto = datafetch.top_mover(crypto_data)
            print(top_crypto)
        except Exception as _:
            print("Base data could not be fetched.")

        
        # Find the top mover
        if crypto_data:
            if top_crypto:
                crypto_name = top_crypto['id']
                #crypto_name = 'bitcoin'
                
                granular_data = datafetch.fetch_granular_data(crypto_name)
                
                #print(granular_data)
                dataplot.plotdata(crypto_name, granular_data)
                print("GRAPH UPDATED")
            else:
                print("No top mover found.")
        else:
            print("Failed to fetch data.")
        
        time.sleep(301)  # Wait for 5 min and 1 sec. Graph shows up in 5 min intervals anyways.


#init render template
@app.route('/')
def index():

    file_path = 'backupStorage/backupGraph.html'
    with open(file_path, 'r') as file:
        defaultFig = file.read()
        file.close()


    return render_template('index.html', graph_html=defaultFig)


if __name__ == "__main__":
    t = threading.Thread(target=periodic_fetch)
    t.daemon = True  # This makes the thread terminate when the main program exits
    t.start()  # Start the thread
    app.run(debug=False, host="127.0.0.1", port=8000)

    





