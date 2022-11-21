from http import client
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket
from classeRobotAlpha import AlphaBot
import time

robot= AlphaBot()

def chatServer():

    with socket(AF_INET, SOCK_STREAM) as s:
        robot.stop()
        s.bind(("0.0.0.0", 5000))
        while True:
            s.listen()
            client, clientAdresss=s.accept()
            print(client)
            msg = client.recv(1024).decode("Utf8")
            print(msg)
            if msg == "avanti":
                robot.forward()
            if msg == "stop":
                robot.stop()
            if msg == "indetro":
                robot.backward()
            if msg == "sinistra":
                robot.left()
            if msg == "destra":
                robot.right()
        s.close()


if __name__ == "__main__":
    chatServer()
