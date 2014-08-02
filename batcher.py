import sys
from sorter import *
from comparator import *
VERIFY = 1

bc = Comparator()
rev = ReverseComparator()

def get_bitonic_merger(n):
  if (n == 1):
    return Sorter(1)

  s = Sorter(n)

  stage = [[i, i + n / 2, bc] for i in xrange(1, 1 + n / 2)]

  s.add_stage(stage, VERIFY)

  m1 = get_bitonic_merger(n / 2)
  m2 = get_bitonic_merger(n / 2)
  m1.combine(m2)

  s.join(m1)

  return s

def get_batcher_network(n):
  if n & (n - 1):
    sys.stderr.write("Not a power of 2. Not doing anything...\n")
    return []

  if (n == 1):
    return Sorter(1)
  else :
    # Sorting halves in ascending and descending order
    s = get_batcher_network(n / 2)
    t = get_batcher_network(n / 2)

    t.comparator_swap()
    s.combine(t)

    merger = get_bitonic_merger(n);

    s.join(merger)

    return s

