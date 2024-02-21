from flask import Flask, render_template, send_from_directory
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

@app.route('/update-graph')
def update_graph():
    directory = os.path.join(app.root_path, 'backupStorage')
    return send_from_directory(directory, 'backupGraph.html')


if __name__ == "__main__":
    logging.info("This is an info message in __main__")
    app.run(debug=False, host="127.0.0.1", port=8000)
    
