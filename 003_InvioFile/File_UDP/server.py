from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet

def scrivi_file(pezzi):
    print(pezzi)

def main():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        finito = False
        pezzi = []
        while not finito:
            dati, da = s.recvfrom(8096)
            pkt = Packet.from_bytes(dati)
            if pkt.stato == Packet.INIZIO:
                pezzi = []
            elif pkt.stato == Packet.CONTINUA:
                pezzi.append(pkt.blocco)
            else:
                scrivi_file(b''.join(pezzi))

if __name__ == "__main__":
    main()