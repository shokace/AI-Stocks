import multiprocessing

# Bind to localhost:8000
bind = "127.0.0.1:8000"

# Set number of workers based on CPU cores
workers = multiprocessing.cpu_count() * 2 + 1

# Set worker class to gthread
worker_class = "gthread"

# Set worker threads
threads = 4

# Log file locations
errorlog = "/home/petarelectro/Vailut/error.log"
accesslog = "/home/petarelectro/Vailut/access.log"

# Log level
loglevel = "info"