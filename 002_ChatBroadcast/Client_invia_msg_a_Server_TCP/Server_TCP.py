from socket import socket, AF_INET, SOCK_STREAM

print("Attendo...")
MAX_SIZE = 7000
PORT = 5000

def Server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", PORT))
        s.listen()
        client, client_address = s.accept()
        print ('Si è connesso: ', client_address)
        print("Server in ascolto")

        messaggio = client.recv(MAX_SIZE)
        clientMsg = "Messagio del Client: "+ messaggio.decode("utf-8")
        print(clientMsg)
        
if __name__ == "__main__":
    Server()