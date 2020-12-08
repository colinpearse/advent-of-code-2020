# python3

# 5)

import os

def bin2int(binarray):
    return int("".join(str(bindigit) for bindigit in binarray), 2)

def frow(trow):
    return bin2int([int(d) for d in list(trow.replace("F","0").replace("B","1"))])
def fcol(tcol):
    return bin2int([int(d) for d in list(tcol.replace("R","1").replace("L","0"))])

def ticket_info(ticket):
    row = frow(ticket[:7])
    col = fcol(ticket[-3:])
    return row, col, (row*8)+col
    
def highest_seat05a(file):
    tickets = os.popen("cat "+file).read().splitlines()
    maxseat = 0
    for ticket in tickets:
        row, col, seat = ticket_info(ticket)
        maxseat = max(maxseat, seat)
    return maxseat

def find_my_seat05b(file):
    tickets = os.popen("cat "+file).read().splitlines()
    seats = set()
    minseat = float("inf")
    maxseat = 0
    for ticket in tickets:
        row, col, seat = ticket_info(ticket)
        minseat = min(minseat, seat)
        maxseat = max(maxseat, seat)
        seats.add(seat)
    for i in range(minseat, maxseat):
        if i not in seats:
            return i
    return -1

ticket_eg1 = "BFFFBBFRRR"  # row 70, column 7, seat ID 567
ticket_eg2 = "FFFBBBFRRR"  # row 14, column 7, seat ID 119
ticket_eg3 = "BBFFBBFRLL"  # row 102, column 4, seat ID 820
advent05a_file = "advent05a.txt"

print (ticket_info(ticket_eg1))          # 70, 7, 567
print (ticket_info(ticket_eg2))          # 14, 7, 119
print (ticket_info(ticket_eg3))          # 102, 4, 820
print (highest_seat05a(advent05a_file))  # 838
print (find_my_seat05b(advent05a_file))  # 714
