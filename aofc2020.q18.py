# python3

# 18)

import os, re

def calcflat(arr):
    v = 0
    op = '+'
    for e in arr:
        if e in ('*','+','-'):
            op = e
        else:
            if   op == '*': v *= int(e)
            elif op == '+': v += int(e)
            elif op == '-': v -= int(e)
    return v

# *, +, - have no pref - calculated left to right
def calc(s):
    arr = re.sub(r'(\*|\+|\-|\d+|\(|\))', r'\1:', s.replace(' ','')).rstrip(':').split(':')
    stack = [[]]
    for e in arr:
        if e.isnumeric(): e = int(e)
        if e == '(':
            stack += [[]]
            continue
        elif e == ')':
            e = calcflat(stack.pop())
        stack[-1] += [e]
    return calcflat(stack.pop())

# + takes precedence over other ops
# treat '+' like parentheses, open:check '+' ahead close:check recent stack(s)
def calc_b(s):
    arr = re.sub(r'(\*|\+|\-|\d+|\(|\))', r'\1:', s.replace(' ','')).rstrip(':').split(':')
    alen = len(arr)
    stack = [[]]
    for i in range(alen):
        e = arr[i]
        if e.isnumeric():
            e = int(e)

        if e == '(':
            stack += [[]]
            continue
        elif e == ')':
            e = calcflat(stack.pop())

        if type(e) == int and i+1 < alen and arr[i+1] == '+':
            stack += [[]]

        stack[-1] += [e]

        while len(stack[-1]) >= 3 and stack[-1][-2] == '+':
            e = calcflat(stack.pop())
            stack[-1] += [e]

    return calcflat(stack.pop())

def calc18a(file):
    a = os.popen("cat "+file).read().splitlines()
    return sum([calc(s) for s in a])
def calc18b(file):
    a = os.popen("cat "+file).read().splitlines()
    return sum([calc_b(s) for s in a])

calc_eg1 = '1 + (2 * 3) + (4 * (5 + 6))'
calc_eg2 = '2 * 3 + (4 * 5)'
calc_eg3 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
calc_eg4 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
calc_eg5 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
advent18a_file = "aofc2020.18a.txt"

print (calc(calc_eg1))           # 51
print (calc(calc_eg2))           # 26
print (calc(calc_eg3))           # 437 
print (calc(calc_eg4))           # 12240
print (calc(calc_eg5))           # 13632
print (calc18a(advent18a_file))  # 16332191652452
print (calc_b(calc_eg1))         # 51
print (calc_b(calc_eg2))         # 46 
print (calc_b(calc_eg3))         # 1445
print (calc_b(calc_eg4))         # 669060
print (calc_b(calc_eg5))         # 23340
print (calc18b(advent18a_file))  # 351175492232654
