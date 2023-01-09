from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet

BUFSIZE = 10

def invia_dati(sock, dest):
    with open("miofile.txt", "rb") as f:
        finito = False
        sock.sendto(Packet(b'', Packet.INIZIO).to_bytes(), dest)
        while not finito:
            dati = f.read(BUFSIZE)
            if not dati:
                sock.sendto(Packet(dati, Packet.CONTINUA).to_bytes(), dest)
            else:
                finito = True
        sock.sendto(Packet(b'', Packet.FINE).to_bytes(), dest)

def main():
    with socket(AF_INET, SOCK_DGRAM) as s:
        invia_dati(s, ("127.0.0.1", 5000))

if __name__ == "__main__":
    main()