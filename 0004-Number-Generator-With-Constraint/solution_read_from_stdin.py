#!/bin/python
import sys


def num_generator(digit):
    threes = 0
    fives = digit
    solution = -1

    while fives >= 0 and threes >=0 and (fives + threes == digit):
        if (threes % 5 == 0) and (fives % 3 == 0):
            solution = fives
            break
        fives = fives - 1
        threes = threes + 1
           
    if solution == -1:
       print -1
       return

    assert(threes + fives == digit)

    str = ''
    for i in range(0, fives):
        str = str + '5'

    for j in range(0, threes):
        str = str + '3'
    print str

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    num_generator(n)


