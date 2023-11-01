import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RA2211003010001_s.bind(('localhost', 9999))
print('Server (UDP) is waiting for connection...')
while True:
    data, clientAddress = RA2211003010001_s.recvfrom(1024)
    print('Received data: {}'.format(data.decode()))
    print('From client address: {}'.format(clientAddress))