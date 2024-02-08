import plotly.graph_objects as go
from plotly.offline import plot
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
        clickmode='event+select',
        dragmode=False,
        xaxis_fixedrange=True,  # Prevents zooming on the x-axis
        yaxis_fixedrange=True,  # Prevents zooming on the y-axis
        title=c_name,
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=False
        ),

        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=False,
            range = [buffered_min_price, buffered_max_price]
        ),

        autosize=True,
        margin=dict(
            autoexpand=True
        ),

        showlegend=False,
        hovermode='x unified',
        plot_bgcolor = "#06014b")
    



        #breakpoint()
        # Show the plot
    config ={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],  # Explicitly remove zoom and pan controls
            'displayModeBar': False,  # Optionally show the modebar, but without zoom/pan controls
            'responsive': False}

    #fig.show(config=config)
    graph_html = plot(fig, output_type='div', include_plotlyjs=True, config=config)

    return graph_html
