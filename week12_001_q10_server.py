import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RA2211003010001_s.bind(('localhost', 8888))
print('UDP Server is waiting for incoming packets...')
while True:
    data, clientAddress = RA2211003010001_s.recvfrom(1024)
    print(f'Received packet from client at {clientAddress}: {data.decode()}')