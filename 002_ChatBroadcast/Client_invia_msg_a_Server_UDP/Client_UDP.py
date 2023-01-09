from socket import socket, AF_INET, SOCK_DGRAM

BUFFER_SIZE = 1024
IP = "127.0.0.1"
PORT = 5000

def Client():
    receiver = (IP, PORT)
    
    with socket(AF_INET, SOCK_DGRAM) as s:
        mex = input("Inserisci il messaggio da inviare: ")
        s.sendto(mex.encode(), receiver)
        print("Messaggio Inviato con successo")

if __name__ == "__main__":
    Client()