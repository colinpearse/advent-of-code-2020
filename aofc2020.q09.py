# python3

# 9)

import os

def check_total(total, aset):
    for n1 in aset:
        n2 = total - n1
        if n2 in aset:
            return True
    return False

def sumcheck(a, pre):
    i1 = 0
    for i2 in range(pre,len(a)):
        if not check_total(a[i2], set(a[i1:i2])):
            return i2, a[i2]
        i1 += 1
    return len(a), -1

def contigcheck(a, pre):
    i2, goal = sumcheck(a, pre)
    while i2 > 0:
        i2 -= 1
        i1 = i2 - 1
        trygoal = goal - (a[i2] + a[i1])
        while i1 > 0:
            if trygoal == 0:
                aset = set(a[i1:i2])
                return min(aset) + max(aset)
            elif trygoal < 0:
                break
            i1 -= 1
            trygoal -= a[i1]
    return -1
    
def sumcheck09a(file, pre):
    a = list(map(int, os.popen("cat "+file).read().splitlines()))
    return sumcheck(a, pre)
def contigcheck09b(file, pre):
    a = list(map(int, os.popen("cat "+file).read().splitlines()))
    return contigcheck(a, pre)

nums_eg = list(map(int, '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.splitlines()))
advent09a_file = "aofc2020.09a.txt"

print (sumcheck(nums_eg, 5))                # 127
print (sumcheck09a(advent09a_file, 25))     # 14144619
print (contigcheck(nums_eg, 5))             # 62
print (contigcheck09b(advent09a_file, 25))  # 1766397
