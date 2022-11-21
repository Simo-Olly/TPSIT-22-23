# Programma server 
import socket
print ("Attendo...")
HOST = '127.0.0.1'       # Nome o IP che rappresenta il server locale
PORT = 5000             # Porta non privilegiata  tra 49152 e 65535

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn, addr = s.accept()
print ('Si è connesso: ', addr)
while True:
    dati = conn.recv(1024)
    if not dati:
        break
    else:
        print ("Il client dice: "+ dati.decode("utf-8"))
        break

s.close()
print('Fine programma')