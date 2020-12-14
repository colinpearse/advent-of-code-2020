# python3

# 14)

import os, re, itertools

def bin2int(binarray):
    return int("".join(str(bindigit) for bindigit in binarray), 2)
def ismask(line):
    return line[1] == 'a'
def getmem(line):
    memi,val = line.split(" = ")
    return int(re.split(r'mem\[(\d+)\]', memi)[1]), int(val)

def getmasks(line):
    smask = line.split(" = ")[1]
    OR  = bin2int([1 if c == '1' else 0 for c in smask])
    AND = bin2int([0 if c == '0' else 1 for c in smask])
    return OR, AND

def getmasks_b(line):
    smask = line.split(" = ")[1]
    AND = bin2int([1 if c == '0' else 0 for c in smask])
    OR  = bin2int([1 if c == '1' else 0 for c in smask])
    mlen = len(smask)
    fbits = [i for i,c in enumerate(smask) if c == 'X']
    bcount = len(fbits)
    combos = []
    for permut in [seq for seq in itertools.product([0,1], repeat=bcount)]:
        bina = [0] * mlen
        for i,v in zip(fbits, permut):
            bina[i] = v
        combos += [bin2int(bina)]
    return AND, OR, combos
    
def calc_mem(a):
    mem = {}
    OR,AND = 0,-1
    for line in a:
        if ismask(line):
            OR,AND = getmasks(line)
        else:
            i,v = getmem(line)
            mem[i] = (v | OR) & AND
    return sum(mem.values())

def calc_mem_b(a):
    mem = {}
    AND,OR = -1,0
    for line in a:
        if ismask(line):
            AND,OR,combos = getmasks_b(line)
        else:
            i,v = getmem(line)
            for fmask in combos:
                i = ((i & AND) | OR) | fmask
                mem[i] = v
    return sum(mem.values())

def calc_mem14a(file):
    a = os.popen("cat "+file).read().splitlines()
    return calc_mem(a)
def calc_mem14b(file):
    a = os.popen("cat "+file).read().splitlines()
    return calc_mem_b(a)

mem_eg = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.splitlines()
mem_eg_b = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.splitlines()
advent14a_file = "aofc2020.14a.txt"

print (calc_mem(mem_eg))             # 165
print (calc_mem14a(advent14a_file))  # 10885823581193
print (calc_mem_b(mem_eg_b))         # 208
print (calc_mem14b(advent14a_file))  # 3816594901962
