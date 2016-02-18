#!/bin/python
import sys
import Queue

class MyQ(object):
    class QLink(object):
         def __init__(self, data, type):
             self.data = data
             self.next = None
             self.type = type

    def __init__(self):
        self.head = self.tail = None
        self.dcount = 0

    def _delete(self, prev, node):
        if prev != None:
            prev.next = node.next
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = node.next

    def deque(self):
        if self.head is None:
            return (None, None)
        node = self.head
        self._delete(None, node)
        return (node.data, node.type)

    def _type_deque(self, type):
        temp = self.head 
        prev = None
        while temp != None and temp.type != type:
            prev = temp
            temp = temp.next
        if temp is None:
            return (None, None)
        self._delete(prev, temp)
        return (temp.data, temp.type)

    def deque_A(self):
        return self._type_deque(type='A')
        
    def deque_B(self):
        return self._type_deque(type='B')

    def enque(self, type, data):
        node = MyQ.QLink(data, type)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def display(self):
        self.dcount = self.dcount + 1
        print("MyQ.display({}) - ".format(self.dcount))
        node = self.head
        while node != None:
            print("Type:{}, Data:{}".format(node.type, node.data))
            node = node.next

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
   
    q = MyQ()
    
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    while True:
        otd = raw_input(input_fp).split() 
        if otd[0] == 'ENQ':
            q.enque(otd[1], otd[2])
        elif otd[0] == 'DEQ':
            print q.deque()
        elif otd[0] == 'TDQ':
            print q._type_deque(otd[1])
        else:
            break
        q.display()
    

if __name__ == '__main__':
    main()
