from sorter import *
from comparator import *

VERIFY = 1

bc = Comparator()

sorter = Sorter(4)

sorter.add_stage(((3, 1, bc), (2, 4, bc)), VERIFY)
sorter.add_stage(((2, 1, bc), (3, 4, bc)), VERIFY)
sorter.add_stage(((3, 2, bc),), VERIFY)

sorter.does_it_sort()
