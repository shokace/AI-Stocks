import yfinance as yf
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
import os

app = Flask(__name__)

class Stock:
    def __init__(self, ticker):
        self.symbol = ticker
        self.start_date = '2000-01-01'
        self.end_date = '2022-12-31'
    
# Define the stock symbol and date range
def getData(stock):

    csv_filename = stock.symbol + '.csv'

    # Download the historical stock data
    stock_data = yf.download(stock.symbol, start=stock.start_date, end=stock.end_date)


    csv_filename = f"{stock.symbol}_historical_data.csv"
    if not (os.path.exists(csv_filename)):
        stock_data.to_csv(csv_filename)

    # Print the first few rows of the data
    print(stock_data.head())

    ##NEXT STEP: GRAPH EVERYTHING (fire emoji, fire emoji, fire emoji)



#init render template
@app.route('/')
def index():
    return render_template('index.html')





@app.route('/process')
def process():
    stock_symbol = request.args.get('stock_symbol')
    # Process stock_arg as needed
    input_Stock = Stock(stock_symbol)
    getData(input_Stock)


    return f"Ticker: {stock_symbol}"





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





