import random
import config
import time

def modexp(a , b, n):
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc * a) % n
        a = (a *a) % n
        b = b // 2
    return acc

# NUMBER -> STRING -> BYTES
def encode_big(num):
    return str(num).encode('utf8')

#STRING -> BYTES -> NUMBER
def decode_big(s):
    return int(s.decode('utf8'))

def dh(sock):

    #GENERO SEGRETO
    b = random.randint(1,config.P-2)

    #GENERO NUMERO PUBBLICO
    gb=modexp(config.G, b, config.P)
    sock.sendall(encode_big(gb))

    ga = decode_big(sock.recv(4096))

    gab= modexp(gb, b, config.P)

    return gab

