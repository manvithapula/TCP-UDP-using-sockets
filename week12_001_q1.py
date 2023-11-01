import socket
RA2211003010001_c=socket.socket()
RA2211003010001_c.connect(('localhost',9999))
data = RA2211003010001_c.recv(1024)
print(data.decode())
RA2211003010001_c.close()