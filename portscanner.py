import socket

# Portscanners scan 1 - 65535
host = socket.gethostname()
port = 22 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)