import random as r
import sys
from math import *

def is_sorted(arr, n):
    return arr == [x + 1 for x in range(n)]

def invcnt(arr):
    ret = 0
    l = len(arr)
    for i in xrange(l):
        for j in xrange(i+1, l):
            if arr[i] > arr[j] :
                ret += 1
    return ret

def get_max_dist(arr, n):
    return max([abs(index + 1 - val) for index, val in enumerate(arr)])

def get_random_perfect_matching(n):
    ret = []
    assert n % 2 == 0
    used = [0] * n
    
    cnt = 0
    while cnt < n:
        i, j = -1, -1
        while i == -1 :
            t = r.randint(0, n-1)
            if used[t] == 0:
                i, used[i] = t, 1

        while j == -1 :
            t = r.randint(0, n-1)
            if used[t] == 0:
                j, used[j] = t, 1

        cnt += 2
        ret.append([i, j])

    return ret

def get_gen_matching(n, i):
    ret = []
    assert n % 2 == 0

    if i == 0:
        ret = [[2*i, 2*i + 1] for i in xrange(n/2)]
        return ret

    else:
        ret = [[2*i + 1, 2*i + 2] for i in xrange(n/2-1)]
        ret.append([0, n - 1])
        return ret

def apply_matching(wires, matching):
    for x, y in matching:
        wires[min(x, y)], wires[max(x, y)] = min(wires[x], wires[y]), max(wires[x], wires[y])

    return wires

n = int(sys.argv[1])
#print n

n = 0
while 1:
    n += 2

    passes = 0
    num_passes = 3

    tot = 0
    while passes < num_passes:

        stage = 0
        arr = [x + 1 for x in range(n)]
        r.shuffle(arr)

        while 1:
            #print "Array after", stage, "stages:"
            #print arr
        
            cnt = invcnt(arr)

            #if is_sorted(arr, n):
            #    tot += stage
            #    break

            if cnt <= n ** 1.5 :
                tot += stage
                break
        
            #if cnt * log(2) <= n * log(n):
            #    tot += stage
            #    break
        
            #print "Number of inversions:", cnt
            #print 
        
            #print "Stage:", stage, "Inversions:", cnt, "Dist:", dist
            #print "Stage:", stage
        
            #if not cnt:
            #    print "Array sorted after", stage, "random matchings..."
            #    break
        
        
            match = get_random_perfect_matching(n)
            #print "Matching chosen:", str(match)
        
            arr = apply_matching(arr, match)
        
            stage += 1
        
            #match = get_gen_matching(n, 0)
            #arr = apply_matching(arr, match)

            #match = get_gen_matching(n, 1)
            #arr = apply_matching(arr, match)

            stage += 2
        
        
        passes += 1

    print n, int(tot / float(num_passes))
