import sys

def flip_bits(a):
    c = ~a & 0xffffffff
    print c
    return c

def raw_input(fp):
    return int(fp.readline().strip().split()[0])

def main(fp=None):
    if fp is None:
       fp = sys.stdin
   
    n = raw_input(fp)
    for i in xrange(0, n):
        a = raw_input(fp)
        flip_bits(a)

if __name__ == '__main__':
   main()
    
