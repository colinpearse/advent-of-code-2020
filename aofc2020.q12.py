# python3

# 12)

import os

def move_ship(moves):
    deg = 90
    x = 0
    y = 0
    for move in moves:
        m,v = move[:1],int(move[1:])
        if   m == 'N': y += v
        elif m == 'S': y -= v
        elif m == 'E': x += v
        elif m == 'W': x -= v
        elif m == 'L': deg = (deg-v)%360
        elif m == 'R': deg = (deg+v)%360
        elif m == 'F':
            if   deg == 0:   y += v
            elif deg == 180: y -= v
            elif deg == 90:  x += v
            elif deg == 270: x -= v
    return abs(x) + abs(y)

def move_ship_b(moves):
    wpx = 10 # wp = waypoint
    wpy = 1
    x = 0
    y = 0
    for move in moves:
        m,v = move[:1],int(move[1:])
        if   m == 'N': wpy += v
        elif m == 'S': wpy -= v
        elif m == 'E': wpx += v
        elif m == 'W': wpx -= v
        elif m == 'F': y += v*wpy; x += v*wpx
        elif m == 'L':
            if   v == 90:  wpx,wpy, = wpy*-1,wpx
            elif v == 180: wpx,wpy, = wpx*-1,wpy*-1
            elif v == 270: wpx,wpy, = wpy,wpx*-1
        elif m == 'R':
            if   v == 90:  wpx,wpy, = wpy,wpx*-1
            elif v == 180: wpx,wpy, = wpx*-1,wpy*-1
            elif v == 270: wpx,wpy, = wpy*-1,wpx
    return abs(x) + abs(y)

def move_ship12a(file):
    a = os.popen("cat "+file).read().splitlines()
    return move_ship(a)
def move_ship12b(file):
    a = os.popen("cat "+file).read().splitlines()
    return move_ship_b(a)

ship_eg = '''F10
N3
F7
R90
F11'''.splitlines()
advent12a_file = "aofc2020.12a.txt"

print (move_ship(ship_eg))            # 25
print (move_ship12a(advent12a_file))  # 1441
print (move_ship_b(ship_eg))          # 286
print (move_ship12b(advent12a_file))  # 61616
