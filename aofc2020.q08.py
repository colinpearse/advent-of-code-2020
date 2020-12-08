# python3

# 8)

import os

def runinf(prog):
    opcs = set()
    opc = 0
    acc = 0
    while 0 <= opc and opc < len(prog):
        opcs.add(opc)
        action,num = prog[opc].split(' ')
        num = int(num)
        if action == "acc":
            acc += num
            opc += 1
        elif action == "jmp":
            opc += num
        elif action == "nop":
            opc += 1
     
        if opc in opcs:
            return True, acc
    return False, acc

def fixinf(prog):
    for opc in range(len(prog)):
        if prog[opc][:3] == "jmp":
            prog[opc] = "nop" + prog[opc][3:]
            isinf,acc = runinf(prog)
            if not isinf:
                return acc
            prog[opc] = "jmp" + prog[opc][3:]
    return -1

def isinf08a(file):
    a = os.popen("cat "+file).read().splitlines()
    return runinf(a)
def isinf08b(file):
    a = os.popen("cat "+file).read().splitlines()
    return fixinf(a)

code_eg = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines()
advent08a_file = "advent08a.txt"

print (runinf(code_eg))            # 5
print (isinf08a(advent08a_file))   # 2080
print (fixinf(code_eg))            # 8
print (isinf08b(advent08a_file))   # 2477
