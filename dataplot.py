import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plotdata(data):

    # Extract timestamps and prices
    timestamps = [datetime.fromtimestamp(ts/1000.0) for ts, price in data['prices']]
    prices = [price for ts, price in data['prices']]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, label='Price', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Price over Time')

    # Format the date on the x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()  # Rotate date labels for better readability

    plt.legend()
    #plt.show()