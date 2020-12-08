# python3

# 2)

import os

def checkpw_a(policy_pw):
    policy, pw = policy_pw.split(': ')
    freq, c = policy.split(' ')
    fmin, fmax = freq.split('-')
    fmin, fmax = int(fmin), int(fmax)
    cmap = dict({(c,0) for c in list(map(chr, range(97,123)))})  # {'a':0, ...etc}
    for pwc in pw:
        cmap[pwc] += 1
    return True if fmin <= cmap[c] and cmap[c] <= fmax else False

def checkpw_b(policy_pw):
    policy, pw = policy_pw.split(': ')
    freq, c = policy.split(' ')
    pos1, pos2 = freq.split('-')
    pos1, pos2 = int(pos1)-1, int(pos2)-1
    return True if (pw[pos1] == c and pw[pos2] != c) or (pw[pos1] != c and pw[pos2] == c) else False

def check_pws(ppws, checkpw_func):
    return [True == checkpw_func(ppw) for ppw in ppws].count(True)

def check_pws02a(file):
    iarr = list(os.popen("cat "+file).read().splitlines())
    return check_pws(iarr, checkpw_a)
def check_pws02b(file):
    iarr = list(os.popen("cat "+file).read().splitlines())
    return check_pws(iarr, checkpw_b)

test02a = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc" ] # a) must be 1 to 3 'a's in string, b) char positions 1 OR 3 must equal the letter
advent02a_file = "advent02a.txt"

print (check_pws(test02a, checkpw_a))   # 2
print (check_pws02a(advent02a_file))    # 458
print (check_pws(test02a, checkpw_b))   # 1
print (check_pws02b(advent02a_file))    # 342
