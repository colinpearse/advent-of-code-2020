# python3

# 16)

import os, re

def get_valid(a):
    rmap = {}     # range map: name->valid_numbers
    valid = set() # all valid numbers
    for line in a:
        if re.match(r'.*: \d.* or ', line):
            field,ranges = line.split(': ')
            rmap[field] = set()
            for rng in ranges.split(' or '):
                f,t = map(int, rng.split('-'))
                rmap[field] |= set(range(f,t+1))
            valid |= rmap[field]
    return rmap, valid

def get_ticketi(a, smatch):
    for i in range(len(a)):
        if re.match(smatch, a[i]):
            return i

def get_tickets(a):
    i = get_ticketi(a, 'nearby tickets:')
    tickets = []
    for line in a[i+1:]:
        tickets += list(map(int, line.split(',')))
    return tickets

def get_valid_tickets(a, invalid):
    myi = get_ticketi(a, 'your ticket:')
    ni  = get_ticketi(a, 'nearby tickets:')
    tickets = []
    tickets += [list(map(int, a[myi+1].split(',')))]
    for line in a[ni+1:]:
        t = list(map(int, line.split(',')))
        if len(set(t) & invalid) == 0:
            tickets += [t]
    return tickets

def vertical_tickets(tgrid):
    vtickets = []
    maxr = len(tgrid)
    maxc = len(tgrid[0])
    for c in range(maxc):
        vticket = set()
        for r in range(maxr):
            vticket.add(tgrid[r][c])
        vtickets += [vticket]
    return vtickets

def get_fmap(rmap, vtickets):
    fmap = {}   # field map: name->ticket_field_indexes
    for name in rmap:
        fmap[name] = set()
    for name in rmap:
        for i in range(len(vtickets)):
            if len(vtickets[i] & rmap[name]) == len(vtickets[i]):
                fmap[name].add(i)
    return fmap

def reduce_fmap(fmap):
    rfmap = {}
    ok = set()
    for name, idxs in sorted(fmap.items(), key=lambda x: len(x[1])):
        idxs -= ok
        ok |= idxs
        rfmap[name] = list(idxs)[0]  # this assumes there is at least one unique mapping
    return rfmap

def ticket_error(a):
    rmap, valid = get_valid(a)
    tickets = get_tickets(a)
    invalid = [t for t in tickets if t not in valid]
    return sum(invalid)

def ticket_fields(a, eg=False):
    rmap, valid = get_valid(a)
    invalid = set(get_tickets(a)) - valid
    tickets = get_valid_tickets(a, invalid)
    vtickets = vertical_tickets(tickets)
    fmap = get_fmap(rmap, vtickets)
    rfmap = reduce_fmap(fmap)
    if eg:
        return rfmap
    else:
        prod = 1
        for name in rfmap:
            if re.match(r'departure ', name):
                prod *= tickets[0][rfmap[name]]
        return prod
    
def ticket_error16a(file):
    a = os.popen("cat "+file).read().splitlines()
    return ticket_error(a)
def ticket_error16b(file):
    a = os.popen("cat "+file).read().splitlines()
    return ticket_fields(a)

notes_eg = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.splitlines()
notes_eg2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.splitlines()
advent16a_file = "aofc2020.16a.txt"

print (ticket_error(notes_eg))            # 71
print (ticket_error16a(advent16a_file))   # 20048
print (ticket_fields(notes_eg2, eg=True)) # {'seat': 2, 'class': 1, 'row': 0}
print (ticket_error16b(advent16a_file))   # 4810284647569
