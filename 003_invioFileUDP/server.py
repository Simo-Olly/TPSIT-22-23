from packet import Packet
from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 131072

def write_file(buffer):
    with open("result.pdf", "wb") as f:
        f.write(buffer)

def run_server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5000))
        file = []

        while True:
            msg = s.recvfrom(MAX_SIZE)
            packet = Packet.from_bytes(msg)
            if packet.status == Packet.NEW_FILE:
                file = []

            if packet.data and len(packet.data) > 0:
                file.append(packet.data)

            if packet.status == Packet.END_FILE:
                write_file(b''.join(file))

if __name__ == "__main__":
    run_server()