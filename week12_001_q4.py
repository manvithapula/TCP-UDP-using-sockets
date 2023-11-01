import socket
import random
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
random_number = random.randint(1, 100)
serverAddress = ('localhost', 9999)
RA2211003010001_c.sendto(str(random_number).encode(), serverAddress)
print(f'Sent random number to the UDP server: {random_number}')
result, serverAddress = RA2211003010001_c.recvfrom(1024)
print(f'Received result from the server: {result.decode()}')
