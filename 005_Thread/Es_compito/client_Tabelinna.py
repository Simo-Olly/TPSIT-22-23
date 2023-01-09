import socket
import time


def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",8000))

    print("Di quale numero vuoi la tabellina ?")
    numeroScelto=input("")
    s.sendall((numeroScelto).encode())

    for i in range(11):
        risultato=s.recv(4096).decode()
        print(risultato)
        time.sleep(1)
    print("exit")

if __name__=="__main__":
    main()