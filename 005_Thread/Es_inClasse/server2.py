import socket
import threading
import time


def funServer(conn,adress):
    print(f"Conesso con {adress}")
    while True:
        msg = conn.recv(4096).decode()
        print(msg)
        if msg == "EXIT":
            conn.close()
            break
        else:
            try:
                risul = eval(msg)
                conn.sendall(str(risul).encode())
            except:
                print("Errore")
                conn.sendall("Errore".encode())



def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    while True:
        conn,adress = server.accept()

        t = threading.Thread(target=funServer, args=(conn,adress,))
        t.start()

if __name__ == "__main__":
    main()