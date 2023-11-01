import socket
import pickle
RA2211003010001_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RA2211003010001_c.connect(('localhost', 9999))
numbers = [1, 2, 3, 4, 5]
data = pickle.dumps(numbers)
RA2211003010001_c.send(data)
result = RA2211003010001_c.recv(1024).decode()
print('Sum of numbers received from the server:', result)
RA2211003010001_c.close()