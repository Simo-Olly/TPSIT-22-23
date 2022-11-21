import socket 

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

 # Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 # Send to server using created UDP socket

def chat_client():
    running = True
    while running == True:
        mex = input("Inserire il messaggio: ")
        bytesToSend = str.encode(mex)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        bytesToSend = str.encode(mex)
        if mex == 'esci' or mex == 'ESCI':
            running = False
        else:
            mex = "Message from Server {}".format(msgFromServer[0])
            print(mex)

if __name__ == "__main__":
    chat_client()