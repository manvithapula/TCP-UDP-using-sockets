import socket
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "UDP Message"
serverAddress = ('localhost', 9999)
RA2211003010001_c.sendto(message.encode(), serverAddress)
print('Message sent to the UDP server:', message)
acknowledgment, serverAddress = RA2211003010001_c.recvfrom(1024)
print('Received acknowledgment from the server:', acknowledgment.decode())