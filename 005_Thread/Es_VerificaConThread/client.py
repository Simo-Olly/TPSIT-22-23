from socket import socket, AF_INET, SOCK_STREAM

def chat_client():
    # legge da file l'indirizzo e la porta
    f = open("confserver.txt","r")
    riga = f.read()
    valori = riga.split(", ")
    indirizzo = valori[0]
    porta = valori[1] 
    receiver = (indirizzo, int(porta))
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        running = True
        while running:
            #invio il messaggio
            messaggio = input('Inserisci il messaggio che vuoi inviare: ')
            s.send(messaggio.encode())
            if messaggio == "fine":
                running = False
            else:
                print("Messaggio inviato")

if __name__ == "__main__":
    chat_client()