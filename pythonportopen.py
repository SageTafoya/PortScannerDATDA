import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.249.9.176"
port = 62800

server_socket.bind((host, port))

server_socket.listen(1)
print(f"Listining for scanner on {host} : {port}")

while True:
    client_socket, addr =server_socket.accept()
    print(f"connected by {addr}")

    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode('utf-8')}")

    client_socket.sendall(b"This is the friggin server yall!")

    client_socket.close()


