import socket
import json

def test_server():
    # Definerer host og port
    host = '127.0.0.1'
    port = 55772

    # Opret socketobjekt
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Forbinder til serveren
    client_socket.connect((host, port))

    # JSON data for et webcam
    webcam_data = {"Id": 1, "Brand": "Logitech", "Height": 1080, "Width": 1920}

    # Sender JSON-strengen til serveren
    client_socket.send(json.dumps(webcam_data).encode('utf-8'))

    # Modtag svar fra serveren
    response = client_socket.recv(1024).decode('utf-8')
    print("Serverens svar:", response)

    # Luk forbindelsen
    client_socket.close()

# Test af serveren
test_server()
