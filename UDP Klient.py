import socket
import json

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 4536)

def send_webcam_data(webcam):
    message = json.dumps(webcam).encode()
    try:
        # Send data
        print(f"\nSending {message}")
        sent = sock.sendto(message, server_address)

        # Receive response
        print("Waiting to receive")
        data, server = sock.recvfrom(4096)
        print(f"Received {data}")

    finally:
        print("Closing socket")
        sock.close()

webcam = {"Id": "6", "Brand": "Logitech", "Height": 720, "Width": 1280}
send_webcam_data(webcam)