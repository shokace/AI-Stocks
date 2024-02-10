import plotly.graph_objects as go
from plotly.offline import plot
from datetime import datetime


def plotdata(c_name, data):


    # Extract timestamps and price
    timestamps = [datetime.fromtimestamp(ts/1000) for ts, price in data['prices']]
    prices = [price for ts, price in data['prices']]


    buffered_min_price = min(prices)-(max(prices)* 0.05)
    buffered_max_price = max(prices)+(max(prices)* 0.05)
    buffer_diff = (buffered_max_price - buffered_min_price)
    
    start_price = prices[0]
    end_price = prices[-1]

    def determine_hover_precision():
        if buffer_diff > 1000:
            return "$,.2f"  # 2 decimal places for large ranges
        elif buffer_diff > 1:
            return "$,.4f"  # 4 decimal places for moderate ranges
        else:
            return "$,.8f"  # 8 decimal places for small ranges
    
    #print("FORMAT: ", determine_hover_precision())

    # Create the plot with Plotly
    if(start_price <= end_price):      
        fig = go.Figure(data=go.Scatter(x=timestamps,
                                        y=prices, 
                                        fill='tozeroy', 
                                        mode='lines', 
                                        line=dict(color='lightseagreen'), 
                                        hovertemplate='%{y:'+ determine_hover_precision() +'}<extra></extra>'))
    else:
        fig = go.Figure(data=go.Scatter(x=timestamps,
                                        y=prices, 
                                        fill='tozeroy', 
                                        mode='lines', 
                                        line=dict(color='red'), 
                                        hovertemplate='%{y:'+ determine_hover_precision() +'}<extra></extra>'))

    # Set plot layout
        
    fig.update_layout(
        clickmode='event+select',
        dragmode=False,
        yaxis_tickformat = determine_hover_precision(),
        xaxis_fixedrange=True,  # Prevents zooming on the x-axis
        yaxis_fixedrange=True,  # Prevents zooming on the y-axis
        title=c_name.capitalize(),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=15, color="white"),
        title_x=0.5,
        xaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False
        ),

        yaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
            tickprefix="$",
            
            range = [buffered_min_price, buffered_max_price]
        ),

        autosize=True,
        margin=dict(l=0, r=0, t=36, b=20),

        showlegend=False,
        hovermode='x unified',
        plot_bgcolor = "#06014b")
    



        #breakpoint()
        # Show the plot
    config ={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],  # Explicitly remove zoom and pan controls
            'displayModeBar': False,  # Optionally show the modebar, but without zoom/pan controls
            'staticPlot': False,
            'responsive': True}

    #fig.show(config=config)
    graph_html = plot(fig, output_type='div', include_plotlyjs=True, config=config)

    return graph_html
