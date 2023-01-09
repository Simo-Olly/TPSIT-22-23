class Packet:

    INIZIO = 0
    CONTINUA = 1
    FINE = 2

    def __init__(self, blocco, stato):
        self.blocco = blocco
        self.stato = stato

    def to_bytes(self):
        return b"".join([self.stato.to_bytes(1, 'big'), len(self.blocco).to_bytes(2, 'big'), self.blocco]) # dimensione bytes dedicati
    
    @staticmethod
    def from_bytes(buffer):
        stato = int.from_bytes(buffer[0:1], 'big')
        lung = int.from_bytes(buffer[1:3], 'big')
        blocco = buffer[3:3 + lung]

        return Packet(blocco, stato)

if __name__ == "__main__":
    pkt = Packet(b'ciao', Packet.INIZIO)
    buffer = pkt.to_bytes()
    pkt2 = Packet.from_bytes(buffer)

    assert(pkt.stato == pkt2.stato)
    assert(pkt.blocco == pkt2.blocco)