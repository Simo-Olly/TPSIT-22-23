import sys
from socket import socket, AF_INET, SOCK_STREAM

BUF_SIZE = 4096

class options:
    def __init__(self, portaServer, host, porta):
        self.portaServer = int(portaServer)
        self.host = host
        self.porta = int(porta)
        

    def get_socket(self):
        return self.host, self.porta
        

def richiediDati(sock, percorso):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sock)
        print("Faccio la richiesta")
        richiesta = f"GET {percorso}.json HTTP/1.0\n\n"
        s.sendall(richiesta.encode("utf-8"))

        data1 = s.recv(BUF_SIZE)
        data2 = s.recv(BUF_SIZE)
        return data1 + data2

        

def main(args):      
    opt = options(args[1], args[2], args[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", opt.portaServer))
        s.listen()

        while True:
            client, client_address = s.accept()
            data = client.recv(BUF_SIZE) 
            data = data.decode("utf-8")
            campi = data.split(" ")

            data = richiediDati(opt.get_socket(), campi[1])
            s.sendall(data)

if __name__ == "__main__":
    main(sys.argv)









