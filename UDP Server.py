import socket
import json

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 4536)
sock.bind(server_address)

webcams = []

while True:
    print("\nWaiting to receive message")
    data, address = sock.recvfrom(4096)

    print("Received %s bytes from %s" % (len(data), address))
    print(data)

    if data:
        webcam = json.loads(data)
        webcams.append(webcam)
        sent = sock.sendto(json.dumps(webcams).encode(), address)
        print("Sent %s bytes back to %s" % (sent, address))