import socket

def main():
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl.connect(("127.0.0.1", 8000))
    while True:

        mex = input("inserisci una operazione: (exit per uscire) ")
        cl.sendall(mex. encode())
        if mex == "EXIT":
            cl.close()
            break

        msg = cl.recv(4096).decode()
        print(msg)
        

if __name__ == "__main__":
    main()