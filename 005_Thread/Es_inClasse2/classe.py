from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

class MyClassThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self) 
        self.conn = conn

    def run(self):
        try:
            while True:
                msg = self.conn.recv(4096).decode()
                if msg == "exit":
                    running = False
                    self.conn.sendall(("uscito".encode()))
                    self.conn.close()
                else:
                    try:
                        risultato = eval(msg)
                        print(f"Risultato operazione: ", risultato)
                        self.conn.sendall((str(risultato).encode()))
                    except:
                        print("Errore, non hai inserito una operazione")
                        self.conn.sendall(("errore".encode()))
                        pass
        except:
            print("Fine")
    
        
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    running = True
    while running:
        conn, address = s.accept()
        print(f"Connesso con {address}")
        t = MyClassThread(conn=conn)
        t.run()

if __name__ == "__main__":
    main()