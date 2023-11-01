import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RA2211003010001_s.bind(('localhost', 9999))
print('Server (UDP) is waiting for connection...')
while True:
    data, clientAddress = RA2211003010001_s.recvfrom(1024)
    received_number = int(data.decode())
    result = "Even" if received_number % 2 == 0 else "Odd"
    print(f'Connected with client at {clientAddress}')
    RA2211003010001_s.sendto(result.encode(), clientAddress)