# python3

# 17)

# NOTE: the 3x3 examples given don't match the same x,y, they are offset, because they are only showing active cubes

import os

def init_actives(cube, dim=3):
    actives = set()
    ylen,xlen = len(cube),len(cube[0])
    for y in range(ylen):
        for x in range(xlen):
            if cube[y][x] == '#':
                if dim == 4:
                    actives.add((x,ylen-(y+1),0,0))
                else: # dim == 3
                    actives.add((x,ylen-(y+1),0))  # reverse y to make the top of the square the higher number
    return actives

def extend_limits(actives, dim=3):
    xmin,xmax,ymin,ymax,zmin,zmax,wmin,wmax = 1,-1,1,-1,1,-1,1,-1
    xs,ys,zs,ws = [],[],[],[]
    for active in actives:
        if dim == 4: x,y,z,w = active
        else:        x,y,z = active; w = 0
        xmin,xmax = min(x,xmin),max(x,xmax)
        ymin,ymax = min(y,ymin),max(y,ymax)
        zmin,zmax = min(z,zmin),max(z,zmax)
        wmin,wmax = min(w,wmin),max(w,wmax)
    limits = [list(range(xmin-1,xmax+2)),list(range(ymin-1,ymax+2)),list(range(zmin-1,zmax+2)),list(range(wmin-1,wmax+2))]
    return limits[:dim]

def check_neighbours(x,y,z,actives):
    acount = 0
    for xp in [-1,0,1]:
        for yp in [-1,0,1]:
            for zp in [-1,0,1]:
                if (xp,yp,zp) != (0,0,0) and (x+xp,y+yp,z+zp) in actives:
                    acount += 1
    return acount
def check_neighbours_4d(x,y,z,w,actives):
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
                    acount = check_neighbours(x,y,z,actives)
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
                        acount = check_neighbours_4d(x,y,z,w,actives)
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
