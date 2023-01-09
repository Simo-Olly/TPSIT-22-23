import random
import config
import time
import sys
from common import *
from socket import socket, AF_INET, SOCK_STREAM

def main(args):
    random.seed(2*int(time.time()))
    if len(args) < 3:
        print(f"Usage: (args[0]) ip port")
        sys.exit(-1)

    address = (args[1], int(args[2]))

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(address)
        gab = dh(s)


if __name__ == "__main__":
    assert(modexp(3, 8, 17) == 16)
    assert(modexp(4, 123, 1001) == 64)



