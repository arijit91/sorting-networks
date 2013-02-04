from sorter import *
from comparator import *

VERIFY = 1

sorter = Sorter((3, 1, 8, 5, 6))
sorter.add_stage(((2, 1), (3, 5)), VERIFY)
sorter.sort()
