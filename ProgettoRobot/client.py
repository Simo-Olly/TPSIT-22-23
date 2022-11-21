from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket

def chatClient():

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(("192.168.0.132", 5000))
        s.send(input().encode("utf8")) 
        s.close()   


if __name__ == "__main__":
    chatClient()
