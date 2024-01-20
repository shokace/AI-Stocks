import plotly.graph_objects as go
from datetime import datetime

def plotdata(c_name, data):

    # Extract timestamps and price
    timestamps = [datetime.fromtimestamp(ts/1000) for ts, price in data['prices']]
    prices = [price for ts, price in data['prices']]

    
    # Extract timestamps and prices

    # Create the plot with Plotly
    fig = go.Figure(data=go.Scatter(x=timestamps, y=prices, mode='lines', line=dict(color='lightseagreen')))

    # Set plot layout
    fig.update_layout(
    title=c_name,
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        title_text = ''
    ),
    yaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        title_text = ''
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
    return c_name, data
