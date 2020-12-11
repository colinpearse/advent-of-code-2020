# python3

# 11)

import os, copy

def _U (a, rmax, cmax, r, c, qty): return a[r-qty][c]     if r-qty >= 0                    else None
def _D (a, rmax, cmax, r, c, qty): return a[r][c-qty]     if c-qty >= 0                    else None
def _L (a, rmax, cmax, r, c, qty): return a[r+qty][c]     if r+qty < rmax                  else None
def _R (a, rmax, cmax, r, c, qty): return a[r][c+qty]     if c+qty < cmax                  else None
def _UL(a, rmax, cmax, r, c, qty): return a[r-qty][c-qty] if r-qty >= 0   and c-qty >= 0   else None
def _UR(a, rmax, cmax, r, c, qty): return a[r-qty][c+qty] if r-qty >= 0   and c+qty < cmax else None
def _DR(a, rmax, cmax, r, c, qty): return a[r+qty][c+qty] if r+qty < rmax and c+qty < cmax else None
def _DL(a, rmax, cmax, r, c, qty): return a[r+qty][c-qty] if r+qty < rmax and c-qty >= 0   else None

def getadj(a, rmax, cmax, r, c, qty):
    return [look(a, rmax, cmax, r, c, qty) for look in [_L, _UL, _U, _UR, _R, _DR, _D, _DL]]

def lookadj(a, rmax, cmax, r, c, qmax):
    adj = []
    for look in [_L, _UL, _U, _UR, _R, _DR, _D, _DL]:
        for qty in range(1,qmax+1):
            seat = look(a, rmax, cmax, r, c, qty)
            if seat == None:
                break
            if seat == 'L' or seat == '#':
                adj += [seat]
                break
    return adj

def change_seat(a, newa, rmax, cmax, r, c):
    if a[r][c] != '.':
        adj = getadj(a, rmax, cmax, r, c, 1)
        if a[r][c] == 'L' and adj.count('#') == 0: newa[r][c] = '#'
        if a[r][c] == '#' and adj.count('#') >= 4: newa[r][c] = 'L'

def change_seat_b(a, newa, rmax, cmax, r, c):
    if a[r][c] != '.':
        adj = lookadj(a, rmax, cmax, r, c, cmax)
        if a[r][c] == 'L' and adj.count('#') == 0: newa[r][c] = '#'
        if a[r][c] == '#' and adj.count('#') >= 5: newa[r][c] = 'L'
            
def conv2d(a, rmax, cmax):
    return [[a[r][c] for c in range(cmax)] for r in range(rmax)]

def joinrows(a):
    joinrows = ''
    for row in a:
        joinrows += ''.join(row)
    return joinrows
        
def printa(a):
    for row in a:
        print (''.join(row))

def change_seats(a, change_seat_func):
    rmax = len(a)
    cmax = len(a[0])
    cura = conv2d(a, rmax, cmax)
    i = 1
    while i:
        newa = copy.deepcopy(cura)
        for r in range(rmax):
            for c in range(cmax):
                change_seat_func(cura, newa, rmax, cmax, r, c)
        if joinrows(cura) == joinrows(newa):
            return list(joinrows(newa)).count('#')
        cura = newa

def change_seats11a(file):
    a = os.popen("cat "+file).read().splitlines()
    return change_seats(a, change_seat)
def change_seats11b(file):
    a = os.popen("cat "+file).read().splitlines()
    return change_seats(a, change_seat_b)

seat_eg = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines()
advent11a_file = "aofc2020.11a.txt"

print (change_seats(seat_eg, change_seat))    # 37
print (change_seats11a(advent11a_file))       # 2238
print (change_seats(seat_eg, change_seat_b))  # 26
print (change_seats11b(advent11a_file))       # 2013
