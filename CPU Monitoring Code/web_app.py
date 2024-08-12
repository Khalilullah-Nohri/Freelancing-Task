# Import necessary libraries
from flask import Flask, render_template
import socket,threading

# Create a Flask application
app = Flask(__name__)

cpu_usage = "0"

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page with the current CPU usage
    return render_template('index.html', cpu_usage=cpu_usage)

def get_cpu_usage():
    
    global cpu_usage
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect(('localhost', 6666))

    # Continuously receive CPU usage from the server and update the global variable
    while True:
        cpu_usage = client_socket.recv(1024).decode()


if __name__ == "__main__":

    # Start a new thread that runs the get_cpu_usage function
    threading.Thread(target=get_cpu_usage).start()
    
    # Start the Flask application
    app.run(port=5000)
