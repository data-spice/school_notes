import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

while True:
    print("Waiting for a client...")
    print()
    print()
    print()

    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    data = client_socket.recv(1024)
    time.sleep(5)
    print(f"Received message: {data.decode()}")

    client_socket.send(b"Hello Client, message received!")

    client_socket.close()
    print("Client disconnected.\n")