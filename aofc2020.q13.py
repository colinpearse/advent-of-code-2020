# python3

# 13)

import os

def get_time_buses(a):
    return int(a[0]), list(map(int, set(a[1].split(',')) - set(['x'])))

def bus_times(a):
    t,buses = get_time_buses(a)
    ttry = t
    while ttry:
        for bus in buses:
            if ttry%bus == 0:
                return ttry-t,bus,(ttry-t)*bus
        ttry += 1
    return None

# pinched from: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def earliest_bus_times(a):
    buses  = [int(b)   for i,b in enumerate(a[1].split(',')) if b != 'x']
    busmod = [int(b)-i for i,b in enumerate(a[1].split(',')) if b != 'x']
    return chinese_remainder(buses, busmod)

def bus_times13a(a):
    return bus_times(a)
def bus_times13b(a):
    return earliest_bus_times(a)

bus_eg = '''939
7,13,x,x,59,x,31,19'''.splitlines()
bus13a_input = '''1005595
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,557,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,419,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'''.splitlines()

print (bus_times(bus_eg))           # (5, 59, 295)
print (bus_times13a(bus13a_input))  # (5, 419, 2095)
print (earliest_bus_times(bus_eg))  # 1068781
print (bus_times13b(bus13a_input))  # 598411311431841
