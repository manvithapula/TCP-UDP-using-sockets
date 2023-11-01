import socket
import time
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 8888)
start_time = time.time()
RA2211003010001_c.connect(serverAddress)
message = "Hello, Server"
RA2211003010001_c.send(message.encode())
response = RA2211003010001_c.recv(1024)
end_time = time.time()
time_taken = end_time - start_time
print('Received response from server:', response.decode())
print(f'Time taken to connect and receive response: {time_taken} seconds')
RA2211003010001_c.close()