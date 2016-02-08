#!/bin/python
import sys


def is_an_array_already_sorted(array, s, e):
    for i in xrange(s, e + 1):
        if array[i] > array[i - 1]:
            continue
        else:
            return False
    return True

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    
def process_array_for_swap(array, n):
    fi = si = 0
    for i in xrange(2, n + 2):
        if array[i] > array[i - 1]:
            continue
        if fi == 0:
            fi = i - 1
        else:
            si = i
            break
    # do temporary swap
    res = False
    if fi != 0 and si != 0:
       swap(array, fi, si)
       res = is_an_array_already_sorted(array, 1, n)
       swap(array, si, fi)
    if res is True:
       print 'yes'
       print('swap {} {}'.format(fi, si))
    return res

def sarr_reverse(array, i, j):
    while i < j:
       swap(array, i, j)
       i = i + 1
       j = j - 1

def process_array_for_subarray_reverse(array, n):
    fi = si = 0
    for i in xrange(2, n + 2):
        if fi != 0: # first inversion found
            if array[i] < array[i - 1]:
                continue
            else:
                si = i - 1
                break
        else:
            if array[i] > array[i - 1]:
                continue
            else:
                fi = i - 1
    # do temporary reverse
    res = False
    if fi != 0 and si != 0:
       if fi == 1 and si == n: # special case detection
          print 'yes'
          if n == 2:
             print('swap {} {}'.format(fi, si))
          else:
             print('reverse {} {}'.format(fi, si))
          return True
       sarr_reverse(array, fi, si)
       res = is_an_array_already_sorted(array, 1, n)
       sarr_reverse(array, si, fi)
    if res is True:
       print 'yes'
       print('reverse {} {}'.format(fi, si))
    return res

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    array = [0]
    input = map(lambda x: int(x), raw_input(input_fp).split()) 
    for x in xrange(0, n):
        array.append(input[x])
    array.append(1000001)
    r = is_an_array_already_sorted(array, 1, n)
    if r is True:
        print 'yes'
    else:
        r = process_array_for_swap(array, n)
        if r is False:
           r = process_array_for_subarray_reverse(array, n)
           if r is False:
              print 'no'

if __name__ == '__main__':
    main()
