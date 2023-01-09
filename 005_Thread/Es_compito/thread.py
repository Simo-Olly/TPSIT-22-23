from threading import Thread
import threading 
import time

luc = threading.Lock()

def funzione():
    print(f"Partenza del thread ", threading.current_thread().name)
    print(f"Elabora....\n ", threading.current_thread().name)
    time.sleep(2)
    print(f"Finito lavoro ",threading.current_thread().name)

def main():
    t = threading.Thread(target=funzione, name="Primo")
    t.start()
    t.join()
    q = threading.Thread(target=funzione, name="Secondo")
    q.start()
    q.join()

    funzione()
    print("Fine chiamata main\n")

if __name__ == "__main__":
    main()