#!/bin/python
import sys
import time
import threading

class Common(object):
    def __init__(self):
        self.mutex = threading.Lock()
        self.cond_var = threading.Condition(self.mutex)
        self.last_done = 0

    def lock(self):
        self.mutex.acquire()

    def unlock(self):
        self.mutex.release()

    def wait(self):
        self.cond_var.wait()

    def notifyAll(self):
        self.cond_var.notifyAll()

def worker(id, com):
    print('Thread-{} has started'.format(id))
    com.lock()
    while com.last_done != id - 1:
        com.wait()
    time.sleep(id)
    com.last_done = id
    com.notifyAll()
    com.unlock()
    print('Thread-{} is done'.format(id))

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    com = Common()
    thrs = []
    for i in range(1, n+1):
        thrs.append(threading.Thread(target=worker, args=[i, com]))
   
    for i in range(n-1, -1, -1):
        thrs[i].start()

    for i in range(0,n):
        thrs[i].join()

if __name__ == '__main__':
    main()
