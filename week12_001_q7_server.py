import socket
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RA2211003010001_s.bind(('localhost', 8888))
RA2211003010001_s.listen(1)
print('TCP Server is waiting for connections...')
while True:
    RA2211003010001_c, clientAddress = RA2211003010001_s.accept()
    print('Connected to', clientAddress)
    data = RA2211003010001_c.recv(1024)
    RA2211003010001_c.send(data)
    RA2211003010001_c.close()
