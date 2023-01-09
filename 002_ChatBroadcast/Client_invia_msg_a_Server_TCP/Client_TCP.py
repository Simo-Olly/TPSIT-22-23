from socket import socket, AF_INET, SOCK_STREAM

BUFFER_SIZE = 1024
IP = "127.0.0.1"
PORT = 5000

def Client():
    receiver = (IP, PORT)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        mex = input("Scrivi messaggio da inviare: ")
        #encodem = mex.encode('utf-8')
        #inviato = s.send(encodem)
        #if (inviato):
        s.send(mex.encode())
        print ("Ho inviato il messaggio con successo")

if __name__ == "__main__":
    Client()
