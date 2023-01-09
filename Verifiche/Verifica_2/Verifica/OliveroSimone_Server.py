from OliveroSimone_Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

print("Attendo...")
MAX_SIZE = 7000

def write_file(buffer):
    with open("result.pdf", "wb") as f:
        f.write(buffer)
   

def Server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 5000))
        s.listen()
        client, client_address = s.accept()
        print ('Si è connesso: ', client_address)
        print("Server in ascolto")

        messaggio = client.recv(MAX_SIZE)
        clientMsg = "Messagio del Client: "+ messaggio.decode("utf-8")
        print(clientMsg)

        running = True
        #arriva il messaggio salva del client ma poi si blocca
        if clientMsg == "Salva":
            while running:
                msg = client.recv(MAX_SIZE)
                packet = Packet.from_bytes(msg)
                
                if packet.status == Packet.NEW_FILE:
                    file = []
                    print('file creato')

                if packet.data and len(packet.data) > 0:
                    file.append(packet.data)
                    print("Pacchetto ricevuto")

                if packet.status == Packet.END_FILE:
                    print("Ricezione pacchetti eseguita")
                    print('inizio scrittura file')
                    write_file(b''.join(file))
                    print("Scrittura file eseguita")
                    running = False
            
if __name__ == "__main__":
    Server()