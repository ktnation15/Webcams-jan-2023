import json
import socket
import threading

def is_16_9(webcam):
    return webcam["Height"] / 9 == webcam["Width"] / 16

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        webcam = json.loads(data.decode())
        print(f"JSON data: {webcam}")
        if is_16_9(webcam):
            client_socket.sendall("Yes".encode())
        else:
            client_socket.sendall("no".encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 55772))
    server.listen()
    print("Server is listening on port 55772...")
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()