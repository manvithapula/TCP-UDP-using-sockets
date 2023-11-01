import socket
RA2211003010001_s=socket.socket()
print('Socket created')
RA2211003010001_s.bind(('localhost',9999))
RA2211003010001_s.listen(3)
print('waiting for connections')
while True:
    c,addr=RA2211003010001_s.accept()
    print('Connected with',addr)
    c.send("Hello, Server!".encode())
    data = c.recv(1024)
    c.close()
    