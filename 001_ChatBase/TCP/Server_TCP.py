# SERVER-TCP

#from Packet import packet
from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 7000

def chat_server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))
        s.listen()
        print("In ascolto")
        client, client_address = s.accept()
        msg = client.recv(MAX_SIZE)
        msg = msg.decode('utf-8')
        print(msg)        
        
if __name__ == "__main__":
    chat_server()