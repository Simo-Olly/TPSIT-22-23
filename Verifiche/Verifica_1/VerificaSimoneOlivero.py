from socket import socket, AF_INET, SOCK_STREAM

PORT = 5000
LOCAL_HOST = 8000

IP = "127.0.0.1"
MAX_SIZE = 7000

def Server():                                                             #Richiesta alla porta 5000             
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((IP, PORT))
        s.listen()
        client, client_address = s.accept()
        print ('è riuscito a connettersi: ', client_address)              #Conferma che si è connesso
        messaggioArrivato = client.recv(MAX_SIZE)
        messaggioConvertito= messaggioArrivato.decode("utf-8")
        print(messaggioConvertito)                                          #Stampa il messaggio arrivato

if __name__ == "__main__":
       Server()


def Client():                                                              #Richiesta porta 8000
    receiver = (IP, LOCAL_HOST)
    sencondaRichiesta =  "GET /data.json HTTP/1.1\n\n"
    with socket(AF_INET, SOCK_STREAM) as c:
        c.connect(receiver)
        c.send(sencondaRichiesta.encode())
        rispostaArrivata = c.recv(MAX_SIZE)
        rispostaArrivata = rispostaArrivata.decode("utf-8")
        print(rispostaArrivata)                                             #Stampa il messaggio arrivato
        

if __name__ == "__main__":
    Client()


