import threading

class ThreadIncrementa(threading.Thread):

    def _init_(self, x):
        threading.Thread._init_(self)
        self.x = x
    def run(self):
        self.x.incrementa()

class Incrementa(threading.Thread):

    def _init_(self, x):
        threading.Thread._init_(self)
        self.x = x
    def incrementa(self):
        for i in range(100000):
            self.x = self.x + 1

if __name__ == "__main__":
    thrs = []
    x = Incrementa(0)
    for i in range(100):
        nome = f"Processo numero {i}"
        thrs.append(ThreadIncrementa(x))
    for t in thrs:
        t.start()
    for t in thrs:
        t.join()

    print(x.x)