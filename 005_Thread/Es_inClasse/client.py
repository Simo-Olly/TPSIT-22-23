import socket

def main():
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl.connect(("127.0.0.1", 8000))

    cl.sendall("4*5". encode())
    risp = cl.recv(4096).decode()
    print(risp)

    

if __name__ == "__main__":
    main()