import plotly.graph_objects as go
from datetime import datetime

def plotdata(c_name, data):

    # Extract timestamps and price
    timestamps = [datetime.fromtimestamp(ts/1000) for ts, price in data['prices']]
    prices = [price for ts, price in data['prices']]

    buffered_min_price = min(prices)-(max(prices)* 0.05)
    buffered_max_price = max(prices)+(max(prices)* 0.05)
    start_price = prices[0]
    end_price = prices[-1]
    # Extract timestamps and prices

    # Create the plot with Plotly
    if(start_price <= end_price):      
        fig = go.Figure(data=go.Scatter(x=timestamps, y=prices, fill='tozeroy', mode='lines', line=dict(color='lightseagreen')))
    else:
        fig = go.Figure(data=go.Scatter(x=timestamps, y=prices, fill='tozeroy', mode='lines', line=dict(color='red')))

    # Set plot layout
    fig.update_layout(
    title=c_name,
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        
        
    ),
    yaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        range = [buffered_min_price, buffered_max_price]
        
    ),
    autosize=True,
    margin=dict(
        autoexpand=True
    ),
    showlegend=False,
    
    hovermode='x unified',
    plot_bgcolor = "#06014b"
    )
    #breakpoint()
    # Show the plot
    fig.show()
    return fig
