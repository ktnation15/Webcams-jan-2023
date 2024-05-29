import json
import socket

def get_webcam_data():
    id = input("Enter webcam id: ")
    brand = input("Enter webcam brand: ")
    height = int(input("Enter webcam height: "))
    width = int(input("Enter webcam width: "))
    return {"Id": id, "Brand": brand, "Height": height, "Width": width}

def send_webcam_data(webcam):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55772))
    client.sendall(json.dumps(webcam).encode())
    response = client.recv(1024).decode()
    client.close()
    return response

def print_response(response):
    if response == "yes":
        print("Is 16/9")
    else:
        print("Is not 16/9")

webcam = get_webcam_data()
response = send_webcam_data(webcam)
print_response(response)