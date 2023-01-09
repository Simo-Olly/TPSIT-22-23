import random
import config
import time
from common import *
from socket import socket, AF_INET, SOCK_STREAM

def mypow(a,b,n):
	return(a ** b) % n


def main():

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5000))
        s.listen()
        client, client_adress = s.accept()

        gab = dh(client)
        print(gab)


if __name__ == "__main__":
    random.seed(int(time.time()))
    main()


