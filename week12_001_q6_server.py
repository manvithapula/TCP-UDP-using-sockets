import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RA2211003010001_s.bind(('localhost', 9999))
print('UDP Server is listening ')
while True:
    data, clientAddress = RA2211003010001_s.recvfrom(1024)
    print(f'Received data from client: {data.decode()}')
    print(f'From client address: {clientAddress}')
    acknowledgment = "Message received by the server"
    RA2211003010001_s.sendto(acknowledgment.encode(), clientAddress)