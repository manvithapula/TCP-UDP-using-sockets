import socket
import pickle
def calculate_sum(numbers):
    return sum(numbers)       
RA2211003010001_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RA2211003010001_s.bind(('localhost', 9999))
RA2211003010001_s.listen(1)
print('Server is listening for connections...')
while True:
    RA2211003010001_c, addr = RA2211003010001_s.accept()
    print('Connected to', addr)
    data = RA2211003010001_c.recv(1024)
    numbers = pickle.loads(data)
    result = calculate_sum(numbers)
    RA2211003010001_c.send(str(result).encode())
    RA2211003010001_c.close()