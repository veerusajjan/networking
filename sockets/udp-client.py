import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = "Hello, Server!"
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

# Receive a response from the server
data, server = client_socket.recvfrom(4096)
print(f"Received from server: {data.decode()}")
