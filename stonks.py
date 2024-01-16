import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import datetime as datetime
import datafetch

from flask import Flask, request, render_template
import os

app = Flask(__name__)

# CoinGecko API endpoint for top 100 cryptocurrencies
tm_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
# Load and Extract JSON data

# Fetch data
crypto_data = datafetch.fetch_crypto_data(tm_url)
top_crypto = datafetch.top_mover(crypto_data)


# Find the top mover
if crypto_data:
    if top_crypto:
        # Plotting
        dates = [datetime.datetime.now() - datetime.timedelta(hours=i) for i in range(24)]
        prices = [top_crypto['current_price']] * 24  # Mock prices as we don't have historical hourly data
        plt.figure(figsize=(10, 6))
        plt.plot(dates, prices, marker='o')
        plt.title(f"Top Mover of the Day: {top_crypto['name']} ({top_crypto['symbol'].upper()})")
        plt.xlabel('Time (Last 24 Hours)')
        plt.ylabel('Price (USD)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
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





