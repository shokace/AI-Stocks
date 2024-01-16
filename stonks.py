import datetime as datetime
import datafetch
import dataplot

from flask import Flask, render_template

app = Flask(__name__)

# CoinGecko API endpoint for top 100 cryptocurrencies
tm_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"

# Fetch data
crypto_data = datafetch.fetch_crypto_data(tm_url)
if crypto_data:
    top_crypto = datafetch.top_mover(crypto_data)
    #print(top_crypto)
else:
    print("Comprehensive data could not be fetched." + crypto_data)




# Find the top mover
if crypto_data:
    if top_crypto:
        crypto_name = top_crypto['name']
        #print(crypto_name)
        granular_data = datafetch.fetch_granular_data(crypto_name)
        #dataplot.plotdata(granular_data) 
        #^^^This has issues...^^^ check the format of the json in granular data. make sure it's formatted correctly in dataplot.py. should fix everything. 
        #################################################################
    else:
        print("No top mover found.")
else:
    print("Failed to fetch data.")



#init render template
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





