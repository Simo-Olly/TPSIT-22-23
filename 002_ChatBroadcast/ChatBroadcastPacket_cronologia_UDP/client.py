from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet

def chatClient(ip, port):
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("Inserisci la frase ('basta' per finire): ")
            if(msg != "basta"):
                pckt = Packet(name, msg)
                packet1 = pckt.to_bytes()

                s.sendto(packet1, (f"{ip}", int(port)))
            else:
                pckt = Packet(name, msg)
                packet1 = pckt.to_bytes()

                s.sendto(packet1, (f"{ip}", int(port)))
                break

if __name__ == "__main__":
    ip = input("Inserisci l'IP: ")
    port = input("Inserisci la porta: ")
    name = input("Inserisci il tuo nickname: ")
    chatClient(ip, port)