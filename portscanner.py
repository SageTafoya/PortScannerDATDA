import socket
import time

# Portscanners scan 1 - 65535
# host = socket.gethostname()
# host = ''
# port = 22 

# # AF_UNSPEC

# # for pport in range(65535)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((host, port))
#     s.sendall(b'Hello World')
#     data = s.recv(1024)
#     s.close
# print('Received', repr(data))


serveraddy = "10.249.9.176"
port = 62800

print(f"Port\t\tState")


for portnum in range(134, 136):
    
    start_time = time.time()

    
    
    try:    
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client_sock.settimeout(10)
        # print("woof")
        client_socket.connect((serveraddy, portnum))
        # print(" ")
        print(f"{portnum}/TCP\t\tOpen")

        
    except:
        # print(f"Failed Connection")
        # print("meow")
        # print(".", end=" ")
        print("", end ="")



    # if client_socket:

    #     client_socket.sendall(b"Hello this is the Hker")

    #     data = client_socket.recv(1024)
    #     print(f"received {data.decode('utf-8')}")

    #     client_socket.close()
    # else:
    #     # print(f"failed to connect to port {port}")
    #     print(".", end=" ")
    end_time = time.time()
    total = end_time - start_time
    print(f"Execution took {total} seconds")