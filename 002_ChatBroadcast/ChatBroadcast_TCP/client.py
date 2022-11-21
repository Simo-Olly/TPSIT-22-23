# Programma client
import socket

HOST = '127.0.0.1'  # Il nodo remoto con nome o IP
PORT = 5000        # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
mex = input("Scrivi il messaggio da inviare: ")
encodem = mex.encode('utf-8')
inviato = s.send(encodem)
if (inviato):
    print ("Ho inviato il messaggio")
s.close()