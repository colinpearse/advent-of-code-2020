# python3

# 17)

# NOTE: the 3x3 examples given don't match the same x,y, they are offset, because they are only showing active cubes

# REFACTOR:
# - stuck with (1) because the others didn't prove significantly faster:
#   1. nc = tuple(map(sum, zip(active, coords)))
#   2. nc = tuple(map(operator.add, check, coords))
#   3. nc = tuple(numpy.add(check, coords))
#
# - originally I used nested for loops <dim> dimensions deep, which was slow.
#   Other solutions cycled through the active cubes incrementing the surrounding cubes "minesweeper" style,
#   which meant only having to search for counts equalling 3 and 2 to activate/deactive those particular cubes.
#   This was far more efficient, so I am using this now.

import os, itertools

def init_actives(cube, dim=3):
    actives = set()
    ylen,xlen = len(cube),len(cube[0])
    for y in range(ylen):
        for x in range(xlen):
            if cube[y][x] == '#':
                actives.add((x,ylen-(y+1))+(0,)*(dim-2))  # reverse y to make the top of the square the higher number
    return actives

# count neighbours of each active cube "minesweeper" style,
# and then look for counts of 3 (active) and 2 (active if active already)
def count_neighbours(actives,dim=3):
    neighbours = {}
    for active in actives:
        for coords in itertools.product(range(-1, 2),repeat=dim):
            if coords != (0,)*dim:
                nc = tuple(map(sum, zip(active, coords)))
                if nc not in neighbours:
                    neighbours[nc] = 0
                neighbours[nc] += 1
    return neighbours

def cycle_cube(cube, ncycles, dim=3):
    actives = init_actives(cube, dim=dim)
    for n in range(ncycles):
        new_actives = set()
        for nb,c in count_neighbours(actives,dim=dim).items():
            if c == 3 or (nb in actives and c == 2):
                new_actives.add(nb)
        actives = new_actives
    return len(actives)

def cycle_cube17a(cube, ncycles):
    return cycle_cube(cube, ncycles)
def cycle_cube17b(cube, ncycles):
    return cycle_cube(cube, ncycles, dim=4)

cube_eg = '''.#.
..#
###'''.splitlines()

advent17a = '''.##..#.#
#...##.#
##...#.#
.##.##..
...#.#.#
.##.#..#
...#..##
###..##.'''.splitlines()

print (cycle_cube(cube_eg, 6))        # 112
print (cycle_cube17a(advent17a, 6))   # 359
print (cycle_cube(cube_eg, 6, dim=4)) # 848
print (cycle_cube17b(advent17a, 6))   # 2228
