from flask import Flask, render_template, request, abort
import schedule
import time
import datetime as datetime
import datafetch
import dataplot
from dotenv import load_dotenv
import os





app = Flask(__name__)

#init render template
@app.route('/')
def index():

    file_path = 'backupStorage/backupGraph.html'
    with open(file_path, 'r') as file:
        defaultFig = file.read()
        file.close()

    print("file was opened")
    print(int(time.time()) - datafetch.current_unix_time)
    if (int(time.time()) - datafetch.current_unix_time >= 600):
        
        tm_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"

        # Fetch data
        try:
            crypto_data = datafetch.fetch_crypto_data(tm_url)
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
                fig = dataplot.plotdata(crypto_name, granular_data)
                print("FIG READY")
                return render_template('index.html', graph_html=fig)
            else:
                print("No top mover found.")
        else:
            print("Failed to fetch data.")

        
        
    return render_template('index.html', graph_html=defaultFig)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8000)

    





