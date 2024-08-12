# Import necessary libraries
import psutil,socket,time


def cpu_monitor():

    # Create a socket object
    # This line creates a new socket using the Internet address family (AF_INET) and the SOCK_STREAM type, which is used for TCP connections.
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    socket_server.bind(('localhost', 6666))
    
    # Set up the socket for listening for incoming connections
    socket_server.listen(1)
    print("CPU Monitor started. Waiting for connection...")
    
    # Wait for a client to connect
    client_socket, addr = socket_server.accept()
    print("Connected to client at ", addr)

    # Continuously monitor CPU usage and send it to the client
    while True:
        # Get the current CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        print("CPU Usage: ", cpu_usage)
        
        # Send the CPU usage to the client
        client_socket.send(str(cpu_usage).encode())
        
        # Wait for a second before the next reading
        time.sleep(2)

if __name__ == "__main__":
    cpu_monitor()
