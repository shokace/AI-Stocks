import yfinance as yf
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'




# Define the stock symbol and date range
stock_symbol = 'AAPL'
start_date = '2000-01-01'
end_date = '2022-12-31'

csv_filename = stock_symbol + '.csv'

# Download the historical stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)


csv_filename = f"{stock_symbol}_historical_data.csv"
if not (os.path.exists(csv_filename)):
    stock_data.to_csv(csv_filename)




# Print the first few rows of the data
print(stock_data.head())
