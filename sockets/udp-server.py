import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"[*] Server UDP listening on {SERVER_IP}:{SERVER_PORT}")

# Server loop
while True:
    data, address = server_socket.recvfrom(4096)
    print(f"Message from {address}: {data.decode()}")
    server_socket.sendto("Acknowledged".encode(), address)
