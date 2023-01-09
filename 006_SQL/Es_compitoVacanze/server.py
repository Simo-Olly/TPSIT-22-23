from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import sqlite3 as sq

def inserisci_utente(userName, password):
    conn = sq.connect("utenti.db")
    curs = conn.cursor() 
    curs.execute("INSERT into UTENTI (Username, Password) values (?, ?)", (userName, password)) 
    conn.commit() 
    conn.close() 
    return True

def login_utente(userName, password):
    conn = sq.connect("utenti.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM UTENTI WHERE Username = ? AND Password = ?", (userName, password))
    conn.commit()
    rows = curs.fetchall()
    conn.close()
    return rows

def ricerca_elemento(elemento):
    conn = sq.connect("utenti.db")
    curs = conn.cursor()

    try:
        curs.execute("SELECT Username FROM UTENTI WHERE Username LIKE ?",  ('%' + elemento + '%',))
    except:
        return False
    conn.commit()
    rows = curs.fetchall()
    conn.close()
    return rows

MAX_SIZE = 7000

def Server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))
        s.listen()
        print("In attesa...")

        client, clientAddress = s.accept()
        print(f"Si è connesso: {clientAddress[0]} con successo alla porta {clientAddress[1]}")
        running = True
        while running:
            messaggioClient = client.recv(MAX_SIZE)
            messaggioClient  = messaggioClient .decode()
            messaggioClient  = messaggioClient .split(";")

            comando = messaggioClient [0]
            name = messaggioClient [1]
            pas = messaggioClient [2]

            if comando == "signup":
                try:
                    valore = inserisci_utente(name, pas)
                    if valore:
                        client.sendall("Utente registrato con successo".encode())
                except:
                    client.sendall("Errore, nome utente o password errati".encode())
            else:
                righe = login_utente(name, pas)
                if len(righe) > 0:
                    client.sendall("Dati inseriti correttamente".encode())
                    richiesta = True
                    while richiesta:
                        msg = client.recv(MAX_SIZE)
                        msg = msg.decode()
                        if msg == "esc":
                            richiesta = False
                        else:
                            ris = ricerca_elemento(msg)
                            if ris == False:
                                client.sendall("Elemento inserito non esistente".encode())
                            else:
                                print(ris)
                                m  = "Elemento trovato: " + ris[0][0]
                                client.sendall(m.encode())
                            
if __name__ == "__main__":
    Server()