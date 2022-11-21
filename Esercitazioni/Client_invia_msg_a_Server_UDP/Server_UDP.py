from socket import socket, AF_INET, SOCK_DGRAM

MAX_SIZE = 7000
PORT = 5000

def Server():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", PORT))
        print("Server in ascolto")
        messaggio = s.recvfrom(MAX_SIZE)
        clientMsg = "Messagio del Client:{}".format(messaggio)
        print(clientMsg)

if __name__ == "__main__":
    Server()