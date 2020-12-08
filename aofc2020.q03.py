# python3

# 3)

import os

def count_trees(board, addr, addc):
    lenr = len(board)
    lenc = len(board[0])
    r,c = 0,0
    count = 0
    while r < lenr:
        if board[r][c%lenc] == '#':
            count += 1
        r += addr
        c += addc
    return count

def count_trees_b(board, addrcs):
    product = 1
    for addr,addc in addrcs:
        product *= count_trees(board, addr, addc)
    return product

def count_trees03a(file):
    board = list(os.popen("cat "+file).read().splitlines())
    return count_trees(board, 1, 3)
def count_trees03b(file, addrcs):
    board = list(os.popen("cat "+file).read().splitlines())
    return count_trees_b(board, addrcs)

# go 2 left 1 down, repeat until past bottom, count # encountered (imagine board is infinitely repeated along x)
test03a = [
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]
advent03a_file = "advent03a.txt"
advent03b_addrcs = [(1,1),(1,3),(1,5),(1,7),(2,1)]  # use this + file from a

print (count_trees(test03a, 1, 3))      # 7
print (count_trees03a(advent03a_file))  # 286
print (count_trees_b(test03a, advent03b_addrcs))          # 336
print (count_trees03b(advent03a_file, advent03b_addrcs))  # 3638606400
