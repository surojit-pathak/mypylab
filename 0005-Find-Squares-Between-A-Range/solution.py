#!/bin/python
import sys
import math


def count_squares(a,b):
    count = 0
    xf = math.sqrt(a)
    x = math.floor(xf)
    if x != xf:
       x = math.ceil(xf)
       a = x * x
    while (a <= b):
       count = count + 1
       x = x + 1
       a = x * x
    print count

t = int(raw_input().strip())
for a0 in xrange(t):
    a, b = map(lambda x: int(x), raw_input().strip().split())
    count_squares(a, b)
