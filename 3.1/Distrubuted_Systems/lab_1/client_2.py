import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Send data to server
client_socket.send(b"Hello Server: Client 2")

# Receive reply
data = client_socket.recv(1024)
print(f"Received reply: {data.decode()}")

# Close connection
client_socket.close()