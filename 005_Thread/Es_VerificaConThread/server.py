from socket import socket, AF_INET, SOCK_STREAM
import threading
import time


class MyClassThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self) 
        self.conn = conn

    def chat_server(self):
    
        running = True
        mes = ""
        while True:
            msg = self.conn.recv(8096)
            msg = msg.decode('utf-8')

            messaggio = msg.split(", ")
            if messaggio[0] != "salva" or messaggio != "leggi":
                mes = messaggio[0]
            if messaggio[0] == "salva":

                f = open("lista.txt","a")
                f.write(str(mes))
                f.close()
                print("Messaggio salvato")
            elif messaggio[0] == "leggi":

                f = open("lista.txt","r")
                lista = f.readlines()
                print("Il primo messaggio della lista è: ", lista[0])
                lista.pop(0)
                
                f = open("lista.txt","w")
                f.write(str(lista))
                f.close()
            else:
                running = False

def main():

    f = open("confserver.txt","r")
    riga = f.read()
    valori = riga.split(", ")
    indirizzo = valori[0]
    porta = valori[1]

    ADDRESS = (indirizzo, int(porta))

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(ADDRESS)
    s.listen()
    running = True
    while running:
        print("In ascolto")
        conn, address = s.accept()
        t = MyClassThread(conn=conn)
        t.chat_server()


        
if __name__ == "__main__":
    main()