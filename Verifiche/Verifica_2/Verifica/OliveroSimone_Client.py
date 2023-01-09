from OliveroSimone_Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM

IP = "127.0.0.1"
PORT = 5000

def Client():

    receiver = (IP, PORT)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        mex = input("Scrivi messaggio da inviare: ")
        s.send(mex.encode())
        print ("Ho inviato il messaggio con successo")

        with open("confServer.pdf", "rb") as f:
            s.send(Packet(Packet.NEW_FILE, b'').to_bytes())
            data = True
            print("Inizio dell'invio dei dati")
            while data:
                data = f.read(4096)
                if data:
                    s.send(Packet(Packet.GO_ON, data).to_bytes())
                    print('Il pacchetto è stato inviato')

            s.send(Packet(Packet.END_FILE, b'').to_bytes())


if __name__ == "__main__":
    Client()





