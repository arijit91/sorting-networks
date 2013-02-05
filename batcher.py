import sys
from sorter import *
from comparator import *

VERIFY = 1

bc = Comparator()
rev = ReverseComparator()

#x = Sorter(4)
#x.add_stage([[1, 2, bc], [3, 4, rev]], VERIFY)
#x.add_stage([[1, 3, bc], [2, 4, bc]], VERIFY)
#x.add_stage([[2, 1, bc], [3, 4, bc]], VERIFY)
#x.does_it_sort()

#x = Sorter(2)
#x.add_stage([[1, 2, bc],], VERIFY)
#
#y = Sorter(2)
#y.add_stage([[1, 2, bc],], VERIFY)
#
#z = Sorter(4)
#z.add_stage([[1, 3, bc], [2, 4, bc]], VERIFY)
#z.add_stage([[2, 3, bc]],  VERIFY)
#
#x.combine(y)
#x.join(z)
#
#x.disp()
#x.does_it_sort()

#y = Sorter(2)
#y.add_stage((1, 2, rev), VERIFY)
#
#x.combine(y)
#x.disp()

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

    stage = [[i, i + n / 2, bc] for i in xrange(1, 1 + n / 2)]

    s.add_stage(stage, VERIFY)

    m1 = get_batcher_network(n / 2)
    m2 = get_batcher_network(n / 2)

    m1.combine(m2)
    s.join(m1)

    return s

x = get_batcher_network(8)
x.disp()
x.does_it_sort()
