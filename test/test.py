import subprocess as sp
from threading import Thread
from queue import Queue, Empty
import time


def getabit(o, q):
    for c in iter(lambda: o.read(1), b''):
        q.put(c)
    o.close()


def getdata(q):
    r = b''
    while True:
        try:
            c = q.get(False)
        except Empty:
            break
        else:
            r += c
    return r


pobj1 = sp.Popen(['python', 'main_test.py'], stdin=sp.PIPE, stdout=sp.PIPE, shell=True)
q1 = Queue()
t1 = Thread(target=getabit, args=(pobj1.stdout, q1))
t1.daemon = True
t1.start()

pobj2 = sp.Popen(['vintbas.exe', 'boga2_test.bas'], stdin=sp.PIPE, stdout=sp.PIPE, shell=True)
q2 = Queue()
t2 = Thread(target=getabit, args=(pobj2.stdout, q2))
t2.daemon = True
t2.start()

while True:
    time.sleep(1)
    s1 = getdata(q1).decode()
    s2 = getdata(q2).decode()
    if s1 != s2:
        print("python: ", s1, end="")
        print("basic: ", s2, end="")
    else:
        print(s2, end="")
    if not t1.is_alive() or not t2.is_alive():
        break
    in_dat = input()
    pobj1.stdin.write(bytes(in_dat, 'utf-8'))
    pobj1.stdin.write(b'\n')
    pobj1.stdin.flush()
    pobj2.stdin.write(bytes(in_dat, 'utf-8'))
    pobj2.stdin.write(b'\n')
    pobj2.stdin.flush()
