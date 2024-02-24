from flask import Flask, render_template, send_from_directory, make_response
from dotenv import load_dotenv
import datetime as datetime
import logging
import os

load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("This is an info message")

@app.route('/')
def index():
    file_path = 'backupStorage/backupGraph.html'
    with open(file_path, 'r') as file:
        defaultFig = file.read()

    return render_template('index.html', graph_html=defaultFig)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/update-graph')
def update_graph():
    directory = os.path.join(app.root_path, 'backupStorage')

    response = make_response(send_from_directory(directory, 'backupGraph.html'))

    # Set headers to prevent caching
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response


if __name__ == "__main__":
    logging.info("This is an info message in __main__")
    app.run(debug=True, host="127.0.0.1", port=8000)
    
