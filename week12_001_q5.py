import socket
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello, UDP Server"
serverAddress = ('localhost', 54321)
RA2211003010001_c.sendto(message.encode(), serverAddress)
print('Message sent to the UDP server:', message)


