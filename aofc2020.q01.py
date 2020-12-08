# python3

# 1)

import os

# O(n) instead of nested for loop O(n^2)
def find_values(iarr, total):
    imap = {}
    for i in iarr:
        imap[i] = total-i
    for k,v in imap.items():
        if v in imap:
            return k,v
    return -1,-1

def find_expenses_n2(iarr):
    n1,n2 = find_values(iarr, 2020)
    return n1*n2

def find_expenses_n3(iarr):
    imap = {}
    for i in iarr:
        n1,n2 = find_values(iarr, 2020-i)
        imap[i] = (n1,n2)
    for k,v in imap.items():
        n1,n2 = v
        if n1 != -1:
            return k*n1*n2
    return None

def expenses01a(file):
    iarr = list(map(int, os.popen("cat "+file).read().splitlines()))
    return find_expenses_n2(iarr)
def expenses01b(file):
    iarr = list(map(int, os.popen("cat "+file).read().splitlines()))
    return find_expenses_n3(iarr)

test01a=[1721, 979, 366, 299, 675, 1456]  # a)1721*299 = 514579, b) 979*366*675 = 241861950
advent01a_file = "aofc2020.01a.txt"

print (find_expenses_n2(test01a))    # 514579
print (expenses01a(advent01a_file))  # 1019904
print (find_expenses_n3(test01a))    # 241861950
print (expenses01b(advent01a_file))  # 176647680
