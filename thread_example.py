#!/usr/bin/python 
 
import threading
import time
import sys

count = 0
def worker(message):
    """ Funcao que eh chamada no thread """
    global count
    while True:
        count = count + 1
        time.sleep(3)


def main():
    try:
        t = threading.Thread(target=worker,args=("thread sendo executada",))
        # Se nao setarmos daemon como True entao o ctrl+c nao vai funcionar pois o daemon deixa a thread dependente
        t.daemon = True
        t.start()
        while True:
            time.sleep(1)
            print(count)
    except(KeyboardInterrupt):
        sys.exit(0)


main()