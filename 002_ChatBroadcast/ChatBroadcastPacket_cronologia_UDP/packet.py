# |1 byte (#username) | username | 2 byte (#messaggio) | messaggio

from mimetypes import init

class Packet:
    def __init__(self, username, message):
        #validazione
        self.username = username
        self.message = message
        
    def to_bytes(self):
        #buffer = b''    #definisce un oggetto bytes vuoto --> cosa similare è: buffer = bytes()

        username_bytes = self.username.encode("utf8")
        buffer = len(username_bytes).to_bytes(1, "big")  #big endian: 1 = quanti byte ; "big" = mantiene l'ordine (le cifre meno significative hanno meno spazio), altrimenti c'è "little", che inverte l'ordine
        buffer = buffer + username_bytes

        message_bytes = self.message.encode("utf8")
        buffer = buffer + len(message_bytes).to_bytes(2, "big")
        buffer = buffer + message_bytes
        return buffer

    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], "big")
        username = buffer[1:username_size+1].decode("utf8")

        message_size = int.from_bytes(buffer[username_size+1: username_size+3], "big")
        message = buffer[username_size + 3: username_size+3+message_size].decode("utf8")
        return Packet(username, message)

#def run_tests():
    #test unitare: test su funzioni
    #pkt0 = Packet("user", "message")
    #pkt1 = Packet.from_bytes(pkt0.to_bytes())
    #assert(pkt0.message == pkt1.message)
    #assert(pkt0.username == pkt1.username)

#if __name__ == "__main__":
#    run_tests()