#!/bin/python

import roman_to_decimal as r2d
import decimal_to_roman as d2r

import random

t = random.randint(10, 100)

while t:
    t = t - 1
    d = random.randint(1, 3999)
    r = d2r.roman_representation(d)
    d1 = r2d.roman_to_decimal(r)
    print d, r, d1
    try:
        assert(d == d1)
    except AssertionError:
        print d, r, d1
        break



