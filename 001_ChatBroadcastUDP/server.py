from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET
from packet import *

BUFFER_SIZE = 1024

mystr = "ciao" # str
# bytes

HOST = "0.0.0.0"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatServer(host, port):
    running = True
    with socket (AF_INET, SOCK_DGRAM) as s:
        s.bind((host, port))
        # s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) LINUX E MACOS
        print('In ascolto')
        while running == True:
            msg = s.recvfrom(BUFFER_SIZE)
            p = Packet.from_bytes(msg[0])
            #msg = msg[0].decode()
            us = str(p.username)
            ms = str(p.message)
            us = "".join(us)
            ms = "".join(ms)
            m = "[" + us + "] " + ms
            print(m)

if __name__ == "__main__":
    chatServer(HOST, PORT)