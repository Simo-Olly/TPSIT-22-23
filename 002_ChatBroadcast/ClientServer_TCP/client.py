import socket
HOST = '127.0.0.1'  
PORT = 5000      
s = socket.socket()
s.connect((HOST, PORT))
s.sendall(b'Testo di prova, andate su salentoplus.it')
dati = s.recv(1024)
print('Dati ricevuti', repr(dati))
s.close()