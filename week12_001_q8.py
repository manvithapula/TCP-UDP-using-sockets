import socket
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 8888)
RA2211003010001_c.connect(serverAddress)
while True:
    message = input('Enter a message to send to the server (or type "exit" to quit): ')
    if message == "exit":
        break
    RA2211003010001_c.send(message.encode())
    response = RA2211003010001_c.recv(1024)
    print('Received response from server:', response.decode())
RA2211003010001_c.close()


