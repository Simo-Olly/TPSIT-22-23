import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 # Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("SERVER in ascolto")

def chat_server():
    running = True
    # Listen for incoming datagrams
    while running == True:

        msg = input("Inserire il messaggio: ")
        bytesToSend = str.encode(msg)
        
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        print(clientMsg)
        # Sending a reply to client

        UDPServerSocket.sendto(bytesToSend, address)

if __name__ == "__main__":
    chat_server()