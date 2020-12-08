# python3

# 7)

import os, re

# {'light red': {'bright white': 1, 'muted yellow': 2}, ..., 'dotted black': {}}
def make_bmap(lines):
    bmap = {}
    for line in lines:
        bag,s = re.split(r' bags contain ', line)
        ibags = s.split(',')
        ibmap = {}
        for ibag in ibags:
            a = re.split(r'(\d+) (.*) +bags*\.*', ibag) # ['', '1', 'bright white', ''] ['no other bags.']
            if len(a) >= 3:
                num = int(a[1])
                ibag = a[2]
                ibmap[ibag] = num
            bmap[bag] = ibmap
    return bmap

def bags_dfs_colour(bmap, sbag, ebag):
    q = [sbag]
    while q:
        bag = q.pop()
        for ibag in bmap[bag].keys():
            if ibag == ebag:
                return True
            q += [ibag]
    return False

def colour_bags(lines):
    bmap = make_bmap(lines)
    count = 0
    for bag in bmap.keys():
        if bags_dfs_colour(bmap, bag, 'shiny gold'):
            count += 1
    return count

# OLD: very inefficient
def colour_bags_b_inefficient(lines):
    bmap = make_bmap(lines)
    count = 0
    q = ['shiny gold']
    while q:
        bag = q.pop()
        for ibag,qty in bmap[bag].items():
            for i in range(qty):
                q += [ibag]
                count += 1
    return count

# better
def colour_bags_b(lines):
    bmap = make_bmap(lines)
    count = 0
    q = [('shiny gold',1)]
    mult = [0]
    while q:
        bag,qty = q.pop()
        for ibag,iqty in bmap[bag].items():
            mult += [qty*iqty]
            q += [(ibag,mult[-1])]
    return sum(mult)

def colour_bags07a(file):
    a = os.popen("cat "+file).read().splitlines()
    return colour_bags(a)
def colour_bags07b(file):
    a = os.popen("cat "+file).read().splitlines()
    return colour_bags_b(a)

bags_eg = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()
bags_eg_b = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.splitlines()
advent07a_file = "aofc2020.07a.txt"

print (colour_bags(bags_eg))             # 4
print (colour_bags07a(advent07a_file))   # 337
print (colour_bags_b(bags_eg))           # 32
print (colour_bags_b(bags_eg_b))         # 126
print (colour_bags07b(advent07a_file))   # 50100
