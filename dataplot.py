import plotly.graph_objects as go
from datetime import datetime

def plotdata(data):

    # Extract timestamps and price
    timestamps = [datetime.fromtimestamp(ts/1000) for ts, price in data['prices']]
    prices = [price for ts, price in data['prices']]

    
    # Extract timestamps and prices

    # Create the plot with Plotly
    fig = go.Figure(data=go.Scatter(x=timestamps, y=prices, mode='lines', name='Price', line=dict(color='lightseagreen')))

    # Set plot layout
    fig.update_layout(
        title='Price over Time',
        xaxis_title='Time',
        yaxis_title='Price'
        )
        

    # Show the plot
    fig.show()
