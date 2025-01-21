import socket

# Portscanners scan 1 - 65535
# host = socket.gethostname()
host = ''
port = 22 

# AF_UNSPEC

# for pport in range(65535)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.sendall(b'Hello World')
    data = s.recv(1024)
    s.close
print('Received', repr(data))