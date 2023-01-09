import socket
import threading
import time

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    while True:
        conn,adress = server.accept()
        print(f"Connesso con {adress}")
        msg = conn.recv(4096)
        risultato = eval(msg)

        print(risultato)
        time.sleep(5)
        conn.sendall((str(risultato).encode()))

if __name__ == "__main__":
    main()