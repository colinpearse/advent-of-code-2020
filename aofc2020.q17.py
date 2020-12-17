# python3

# 17)

# NOTE: the 3x3 examples given don't match the same x,y, they are offset, because they are only showing active cubes

# REFACTOR: stopped refactoring for multiple dimensions because check_neighbours(check,actives,dim=4)
#           ran too slowly. I tried using operator and numpy and it didn't improve the speed:
#           neighbour = tuple(map(operator.add, check, coords))
#           neighbour = tuple(numpy.add(check, coords))
#           Will have to revisit...

import os, itertools

def init_actives(cube, dim=3):
    actives = set()
    ylen,xlen = len(cube),len(cube[0])
    for y in range(ylen):
        for x in range(xlen):
            if cube[y][x] == '#':
                actives.add((x,ylen-(y+1))+(0,)*(dim-2))  # reverse y to make the top of the square the higher number
    return actives

# return: [[-2,-1,0,1], [0,1,2,3], ... ] corresponding to x,y,...etc needing to be checked
def extend_limits(actives, dim=3):
    minmax = [[1,-1]]*dim   # [[1, -1], [1, -1], [1, -1], [1, -1], ...]
    for active in actives:
        for i in range(len(active)):
            vdim = active[i]   # vdim will have x,y,z,w,... etc values
            cmin,cmax = minmax[i][0],minmax[i][1]
            minmax[i][0],minmax[i][1] = min(vdim,cmin),max(vdim,cmax)
    return [list(range(minmax[i][0]-1,minmax[i][1]+2)) for i in range(len(minmax))]

# check_neighbours(..., dim=4) is SLOW compared to check_neighbours_4d()
def check_neighbours(check,actives,dim=3):
    acount = 0
    for coords in itertools.product(range(-1, 2),repeat=dim):
        if coords != (0,)*dim:
            neighbour = tuple(map(sum, zip(check, coords)))
            if neighbour in actives:
                acount += 1
    return acount
def check_neighbours_4d(check,actives,dim=4):
    x,y,z,w = check
    acount = 0
    for xp in [-1,0,1]:
        for yp in [-1,0,1]:
            for zp in [-1,0,1]:
                for wp in [-1,0,1]:
                    if (xp,yp,zp,wp) != (0,0,0,0) and (x+xp,y+yp,z+zp,w+wp) in actives:
                        acount += 1
    return acount
    
def cycle_cube(cube, ncycles):
    actives = init_actives(cube)
    for n in range(ncycles):
        xs,ys,zs = extend_limits(actives)
        new_actives = set()
        for x in xs:
            for y in ys:
                for z in zs:
                    acount = check_neighbours((x,y,z),actives,dim=3)
                    if (x,y,z) in actives:
                        if acount == 2 or acount == 3:
                            new_actives.add((x,y,z))
                    else:
                        if acount == 3:
                            new_actives.add((x,y,z))
        actives = new_actives
    return len(actives)

def cycle_cube_4d(cube, ncycles):
    actives = init_actives(cube, dim=4)
    for n in range(ncycles):
        xs,ys,zs,ws = extend_limits(actives, dim=4)
        new_actives = set()
        for x in xs:
            for y in ys:
                for z in zs:
                    for w in ws:
                        acount = check_neighbours_4d((x,y,z,w),actives,dim=4)
                        if (x,y,z,w) in actives:
                            if acount == 2 or acount == 3:
                                new_actives.add((x,y,z,w))
                        else:
                            if acount == 3:
                                new_actives.add((x,y,z,w))
        actives = new_actives
    return len(actives)

def cycle_cube17a(cube, ncycles):
    return cycle_cube(cube, ncycles)
def cycle_cube17b(cube, ncycles):
    return cycle_cube_4d(cube, ncycles)

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

print (cycle_cube(cube_eg, 6))       # 112
print (cycle_cube17a(advent17a, 6))  # 359
print (cycle_cube_4d(cube_eg, 6))    # 848
print (cycle_cube17b(advent17a, 6))  # 2228
