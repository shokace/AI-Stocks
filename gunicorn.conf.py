# gunicorn.conf.py

# Specify the address and port for Gunicorn to listen on
bind = '127.0.0.1:8000'

# Number of worker processes Gunicorn should spawn
workers = 2


app = 'stonks:app'

# Enable capturing output to display in console
capture_output = True