import socket
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ('localhost', 8888)
messages = [
    "UDP Packet 1",
    "UDP Packet 2",
    "UDP Packet 3",
    "UDP Packet 4"
]
for message in messages:
    RA2211003010001_c.sendto(message.encode(), serverAddress)
    print(f'Sent UDP packet to the server: {message}')
RA2211003010001_c.close()