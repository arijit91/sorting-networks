from sorter import *
from comparator import *
from batcher import *
from random import *

VERIFY = 1
seed()

numLines = 4

bc = Comparator()
#fc = FaultyComparator(0.1)
#rc = ReverseComparator()
sorter = Sorter(numLines)

sorter.add_stage(((2, 1, bc), (3, 4, bc)), VERIFY)
sorter.add_stage(((3, 1, bc), (2, 4, bc)), VERIFY)
sorter.add_stage(((3, 2, bc),), VERIFY)

#sorter = get_batcher_network(8)

reverse_sorter = Sorter(numLines)
reverse_sorter.stages = sorter.stages[::-1]

reverse_sorter.does_it_sort()
reverse_sorter.display_ascii_art()

sorter.does_it_sort()
sorter.display_ascii_art()
#print sorter.get_inversions_rating()
#print sorter.get_maxinv_rating()
