from socket import socket, AF_INET, SOCK_STREAM

def chat_server():
    # legge da file l'indirizzo e la porta
    f = open("confserver.txt","r")
    riga = f.read()
    valori = riga.split(", ")
    indirizzo = valori[0]
    porta = valori[1]
    #salvo nella variabile ADDRESS l'indirizzo e la porta
    ADDRESS = (indirizzo, int(porta))    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()
        print("In ascolto")
        client, client_address = s.accept()
        #creo un ciclo for per mantenere in ascolto il server
        running = True
        while running:
            msg = client.recv(8096)
            msg = msg.decode('utf-8')
            #splitto il messaggio e controllo la prima posizione
            messaggio = msg.split(", ")
            if messaggio[0] == "salva":
                #se è "salva" stampo in coda al file il messaggio
                f = open("lista.txt","a")
                f.write(str(msg))
                f.close()
                print("Messaggio salvato")#non sono riuscito ad incolonnare i messaggi
            elif messaggio[0] == "leggi":
                #se è "leggi" lego la prima riga del file e con pop la elimino
                f = open("lista.txt","r")
                lista = f.readlines()
                print("Il primo messaggio della lista è: ", lista[0])
                lista.pop(0)
                
                f = open("lista.txt","w")
                f.write(str(lista))
                f.close()
            else:
                running = False
        
if __name__ == "__main__":
    chat_server()