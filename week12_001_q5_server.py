import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RA2211003010001_s.bind(('localhost', 54321))
print('UDP Server is listening on port 54321...')
while True:
    data, clientAddress = RA2211003010001_s.recvfrom(1024)
    print(f'Received data: {data.decode()}')
    print(f'From client address: {clientAddress}')


