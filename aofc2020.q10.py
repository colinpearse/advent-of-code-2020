# python3

# 10)

import os

def jolt_diffs(a):
    a = [0] + a
    a.sort()
    a += [max(a)+3]
    diffs = {}
    for i in range(1,len(a)):
        d = a[i] - a[i-1]
        if d not in diffs: diffs[d] = 0
        diffs[d] += 1
    return diffs, diffs[1]*diffs[3], a[-1]

# runs together mean differernt combinations: 11=2 111=4 1111=7 combinations
def jolt_arrange(a):
    a = [0] + a
    a.sort()
    a += [max(a)+3]
    diffs1 = []
    diffruns = []
    run1 = 0
    for i in range(1,len(a)):
        d = a[i] - a[i-1]
        if d == 1:
            run1 += 1
        else:
            diffruns += [run1]
            run1 = 0
        diffs1 += [1] if d == 1 else ['|']
    combos = 1
    for diffrun in diffruns:
        if   diffrun == 2: combos *= 2
        elif diffrun == 3: combos *= 4
        elif diffrun == 4: combos *= 7
    return combos, diffruns
    
def jolt_diffs10a(file):
    a = list(map(int, os.popen("cat "+file).read().splitlines()))
    return jolt_diffs(a)
def jolt_arrange10b(file):
    a = list(map(int, os.popen("cat "+file).read().splitlines()))
    return jolt_arrange(a)

jolt_eg1 = list(map(int, '''16
10
15
5
1
11
7
19
6
12
4
'''.splitlines()))
jolt_eg2 = list(map(int, '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.splitlines()))
advent10a_file = "aofc2020.10a.txt"

print (jolt_diffs(jolt_eg1))             # {1: 7 3: 5}, 35, 22
print (jolt_diffs(jolt_eg2))             # {1: 22, 3: 10}, 220, 52
print (jolt_diffs10a(advent10a_file))    # {1: 72, 3: 37}, 2664, 183
print (jolt_arrange(jolt_eg1))           # 8
print (jolt_arrange(jolt_eg2))           # 19208
print (jolt_arrange10b(advent10a_file))  # 148098383347712
