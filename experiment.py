from itertools import chain, combinations
import copy
import sys

def CountInversions(perm):
  cnt = 0
  for i in xrange(len(perm)):
    for j in xrange(i):
      if (perm[j] > perm[i]):
        cnt += 1
  return cnt

def CountInversionDist(perm):
  cnt = 0
  for i in xrange(len(perm)):
    for j in xrange(i):
      if (perm[j] > perm[i]):
        cnt += (i - j)
  return cnt

def Count(perm, metric):
  if (metric == "inversions"):
    return CountInversions(perm)
  if (metric == "inversion_distance"):
    return CountInversionDist(perm)
  assert False

def GenerateMatchings(size):
  assert (size % 2 == 0)
  result = []
  if (size == 0):
    return result
  if (size == 2):
    return [[[0, 1]]]
  matchings = GenerateMatchings(size - 2)
  for i in range(1, size):
    for perm in matchings:
      matching = copy.deepcopy(perm)
      for index, (x, y) in enumerate(matching):
        matching[index][0] += 1
        matching[index][1] += 1
        if (x + 1 >= i):
          matching[index][0] += 1
        if (y + 1 >= i):
          matching[index][1] += 1

      matching.append([0, i])
      result.append(matching)
  return result

def GenerateBinarySequences(size):
  result = []
  if (size == 0):
    return result
  if (size == 1):
    return [[0], [1]]
  seqs = GenerateBinarySequences(size - 1)
  for seq in seqs:
    zero = seq[:]
    one = seq[:]
    zero.append(0)
    one.append(1)
    result.append(zero)
    result.append(one)
  return result

def SimulateStage(stage, matching):
  final = copy.deepcopy(stage)
  for elem in matching:
    assert (elem[0] < elem[1])

    lo = min(stage[elem[0]], stage[elem[1]])
    hi = max(stage[elem[0]], stage[elem[1]])

    final[elem[0]] = lo
    final[elem[1]] = hi

  return final

def GenerateOneShotMatching(size, start):
  result = []
  while (start + 1 < size):
    result.append([start, start + 1])
    start += 2
  return result

def GenerateDiffMatching(size, diff):
  result = []
  used = set()
  for i in range(size):
    lo = min(i, (i + diff) % size)
    hi = max(i, (i + diff) % size)
    if ((lo not in used) and (hi not in used)):
      used.add(lo)
      used.add(hi)
      result.append([lo, hi])
  return result

def GenerateOffsetMatching(matching, offset, size):
  result = []
  for x, y in matching:
    lo = min((x + offset) % size, (y + offset) % size)
    hi = max((x + offset) % size, (y + offset) % size)
    result.append([lo, hi])
  return result

#### Expt: Inversions and Inversion dists wrt matchings
#### size = 10
#### INF = 10**9
#### matchings = GenerateMatchings(size)
#### inputs = GenerateBinarySequences(size)
#### 
#### print len(matchings), len(inputs), len(matchings) * len(inputs)
#### raw_input()
#### #sys.exit(0)
#### 
#### metric = "inversions"
#### #metric = "inversion_distance"
#### cnt = 0
#### highest = INF
#### best = []
#### for m1 in matchings:
####   for m2 in matchings:
####     ratio = 0
####     for stage in inputs:
####       old = stage
####       init = Count(stage, metric)
#### 
####       stage = SimulateStage(stage, m1)
####       stage = SimulateStage(stage, m2)
####       #stage = SimulateStage(stage, GenerateOneShotMatching(size, 0))
####       #stage = SimulateStage(stage, GenerateOneShotMatching(size, 1))
####   
####       final = Count(stage, metric)
####   
####       if (init > 0):
####         if (ratio < final / float(init)):
####           best = [old, init, final]
####         ratio = max(ratio, final / float(init))
####   
####     if (highest > ratio):
####       highest = ratio
####       print m1, m2, ratio
####       print best
####   
####     highest = min(highest, ratio)
####   
####     #print matching, ratio
####     #print
#### 
#### print highest

#### Expt: How does this particular matching do?
size = 32
INF = 10**9
inputs = GenerateBinarySequences(size)
ratio = 0
#metric = "inversions"
metric = "inversion_distance"
print "Generation done..."

for stage in inputs:
  old_stage = stage
  init = Count(stage, metric)

  for i in xrange(1):
    stage = SimulateStage(stage, GenerateDiffMatching(size, 1))
    stage = SimulateStage(stage, GenerateDiffMatching(size, 3))
    stage = SimulateStage(stage, GenerateDiffMatching(size, 7))
    stage = SimulateStage(stage, GenerateDiffMatching(size, 15))
    stage = SimulateStage(stage, GenerateDiffMatching(size, 31))

  final = Count(stage, metric)

  if (init > 0):
    ratio = max(ratio, final / float(init))

print ratio
