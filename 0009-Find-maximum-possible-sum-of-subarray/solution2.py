def find_maximum_sum_of_subarray(arr):
    n = len(arr)
    dp_tab = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    max = [0 for i in xrange(0, n)]
    for i in xrange(0, n):
        max[i] = dp_tab[i][i] = arr[i]
        for j in xrange(i + 1, n):
            dp_tab[i][j] = dp_tab[i][j-1] + arr[j]
            if dp_tab[i][j] > max[i]:
                max[i] = dp_tab[i][j]
  
    mss = max[0]
    ps = 0
    if arr[0] > 0:
       ps = arr[0]
    for i in xrange(1, n):
        if max[i] > mss:
           mss = max[i]
        if arr[i] > 0:
           ps = ps + arr[i]
    
    print mss, ps
    return (mss, ps)
