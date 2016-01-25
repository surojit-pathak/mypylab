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

file = open('./input', 'r+')
first = True
test_num = 0
test_max = 0
for line in file.readlines():
    if first:
        first = False
        test_max = int(line.rstrip())
        # print("test_max: {} ".format(test_max))
        if (test_max < 1) or (test_max > 20):
            print("Test: {} is not allowed".format(test_max))
            break
    else:
        digit = int(line.rstrip())
        if digit >= 1 and digit <= 100000:
           num_generator(digit)
           test_num = test_num + 1
           #print test_num, test_max
           if (test_num >= test_max):
               break
        else:
           print("Digit: {} is not allowed".format(digit))
