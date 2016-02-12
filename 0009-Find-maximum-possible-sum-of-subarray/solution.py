import sys

def find_maximum_sum_of_subarray(arr):
    moving_sum = max_sum = arr[0]
    if arr[0] > 0:
       max_positive_sum = arr[0]
    else:
       max_positive_sum = 0
    si = ei = idx = 0
    for x in arr[1:]:
        idx = idx + 1
        if moving_sum + x > x:
           moving_sum = moving_sum + x
           ei = idx
        else:
           moving_sum = x
            
        if moving_sum > max_sum:
           max_sum = moving_sum
        else:
           ei = idx - 1

        if max_sum == x:
           si = ei = idx

        if x > 0:
           max_positive_sum = max_positive_sum + x

    #print arr[si:ei+1]
    print max_sum, max_positive_sum
    #return (max_sum, max_positive_sum)
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    t = map(lambda x: int(x), raw_input(input_fp).split())[0]
    for i in xrange(0, t):
        n = map(lambda x: int(x), raw_input(input_fp).split())[0]
        input = map(lambda x: int(x), raw_input(input_fp).split()) 
        find_maximum_sum_of_subarray(input)

if __name__ == '__main__':
    main()
