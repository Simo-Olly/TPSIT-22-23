import threading
import socket
import time



def serverFunz(conn,adress):
    print(f"Connesso con {adress}")
    msg = conn.recv(4096).decode()

    for i in range(11):
        risul = int(msg)*int(i)
        tabellina = str(msg)+"*"+str(i)+"="+str(risul)
        print(tabellina)
        i=i+1
        conn.sendall(str(tabellina).encode())
        time.sleep(1)
    print("uscito")


def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("127.0.0.1",8000))
    server.listen()
    while True:
        conn, adress = server.accept()
        t=threading.Thread(target=serverFunz,args=(conn,adress,))
        t.start()

if __name__=="__main__":
    main()
