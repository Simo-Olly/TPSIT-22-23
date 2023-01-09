from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 4098

def Client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        running = True
        print("Inizio invio dati")
        while running:
            comando = input("Inserisci un comando ('signup' - 'login' - 'esc'): ")

            if comando == "signup" or comando == "login": 
                errore = True
                while errore:
                    username = input("Inserisci un nome utente: ")
                    password = input("Inserisci una password: ")
                    messaggio = comando + ";" + username + ";" + password
                    s.send(messaggio.encode())
                    mex = s.recv(MAX_SIZE)
                    mex = mex.decode()
                    print(mex)
                    if "Errore" in mex:
                        print("Inserire nuovamente i dati")
                    else:
                        uscita = True
                        if comando == "login":
                            while uscita:
                                elemento = input("Inserisci elemento da ricercare: ")
                                if elemento == "esc":
                                    uscita = False
                                s.send(elemento.encode())
                                msg = s.recv(MAX_SIZE)
                                msg = msg.decode()
                                print(msg)
                        errore = False
            elif comando == "esc":
                running = False                

if __name__ == "__main__":
    Client()