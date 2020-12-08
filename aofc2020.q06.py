# python3

# 6)

import os

# "anyone"   makes: [{'b', 'a', 'c'}, {'b', 'a', 'c'}, {'b', 'a', 'c'}, {'a'}, {'b'}]
# "everyone" makes: [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
def make_aarr(s, op="anyone"):
    aarr = []
    for astr in s.split('\n\n'):
        if op == "anyone":
            ans = set()
        else: # otherwise "everyone"
            ans = []
        for a in astr.split():
            if op == "anyone":
                ans |= set(list(a))
            else: # otherwise "everyone"
                ans += [a]
        aarr += [ans.copy()]
    return aarr

def count_answers(s):
    return sum([len(ans) for ans in make_aarr(s)])

def count_answers_b(s):
    count = 0
    for group in make_aarr(s, op="everyone"):
        amap = dict({(c,0) for c in list(map(chr, range(97,123)))})  # {'a':0, ...etc}
        for person in group:
            for a in set(list(person)):
                amap[a] += 1
        for aqty in amap.values():
            if len(group) == aqty:
                count += 1
    return count
    
def answer_count06a(file):
    s = os.popen("cat "+file).read()
    return count_answers(s)
def answer_count06b(file):
    s = os.popen("cat "+file).read()
    return count_answers_b(s)
    
answers_eg = '''
abc

a
b
c

ab
ac

a
a
a
a

b'''
    
advent06a_file = "advent06a.txt"

print (count_answers(answers_eg))        # 11
print (answer_count06a(advent06a_file))  # 6170
print (count_answers_b(answers_eg))      # 6
print (answer_count06b(advent06a_file))  # 2947
