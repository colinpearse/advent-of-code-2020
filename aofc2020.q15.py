# python3

# 15)

import os

# not elegant or quick but hey ho

def say_numbers(start, stop, debug=False):
    def setmap(m, n, i):
        m[n] = i
        return n, i+1
    
    sarr = list(map(int, start.split(',')))
    n1map = {}
    n2map = {}
    lastnum = -1
    i = 1
    
    # set start - everything in n1map
    for n in sarr:
        lastnum, i = setmap(n1map, n, i)

    # 0 or 0 0 depending
    if 0 not in n1map:
        lastnum, i = setmap(n1map, 0, i)
    lastnum, i = setmap(n2map, 0, i)
        
    for i in range(i,stop+1):
        if debug and i%1000000 == 0:
            print("i=%d  \r"%(i), end='')

        if lastnum in n2map:
            n = n2map[lastnum] - n1map[lastnum]
            if n in n2map:
                n1map[n] = n2map[n]
                lastnum, i = setmap(n2map, n, i)
            elif n in n1map:
                lastnum, i = setmap(n2map, n, i)
            else:
                lastnum, i = setmap(n1map, n, i)
        else:
            # lastnum in n1map means it's just been put in there
            n = 0
            n1map[n] = n2map[n]
            lastnum, i = setmap(n2map, n, i)

    if debug:
        print("                               \r", end='')

    return lastnum

def say_numbers15a(start, stop):
    return say_numbers(start, stop)
def say_numbers15b(start, stop, debug=True):
    return say_numbers(start, stop, debug=debug)

advent15a = '2,20,0,4,1,17'

print (say_numbers('0,3,6', 2020))       # 436
print (say_numbers('1,3,2', 2020))       # 1
print (say_numbers('2,1,3', 2020))       # 10
print (say_numbers('1,2,3', 2020))       # 27
print (say_numbers('2,3,1', 2020))       # 78
print (say_numbers('3,2,1', 2020))       # 438
print (say_numbers('3,1,2', 2020))       # 1836
print (say_numbers15a(advent15a, 2020))  # 758

# print (say_numbers('0,3,6', 30000000))       # 175594
# print (say_numbers('1,3,2', 30000000))       # 2578
# print (say_numbers('2,1,3', 30000000))       # 3544142
# print (say_numbers('1,2,3', 30000000))       # 261214
# print (say_numbers('2,3,1', 30000000))       # 6895259
# print (say_numbers('3,2,1', 30000000))       # 18
# print (say_numbers('3,1,2', 30000000))       # 362
print (say_numbers15b(advent15a, 30000000))  # 814
