import socket
# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
# Receiving data from server
data = client_socket.recv(1024)
print(f"Received message: {data.decode()}")
# Closing connection
client_socket.close()