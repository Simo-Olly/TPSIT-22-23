from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet

BUFFER_SIZE = 1024

HOST = "0.0.0.0"
#possibilità
#localhost 127.0.0.1 (da esterno nessuno vede)
#fare un bind di un'interfaccia particolare
#ascoltare qualsiasi cosa

def chatServer(port):
    with socket(AF_INET, SOCK_DGRAM) as s:    #SOCK_DGRAM = datagramma socket; SOCK_STREAM = flusso di dati (stream)
        s.bind((HOST, int(port)))                  #nella tupla non si possono mettere altri valori
        
        while True:
            msg = s.recvfrom(BUFFER_SIZE)
            pckt = Packet(msg)              #msg è una variabile 'bytes', perciò facciamo il decode a stringa
            pckt1 = pckt.from_bytes()
            
            if(msg != 'basta'):
                print(pckt1)
                file = open("cronologia.csv", "a")
                file.write(pckt1+"\n")
                file.close()
            else:
                break

if __name__ == "__main__":
    port = input("Inserisci la porta: ")
    chatServer(port)