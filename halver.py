from comparator import *
from sorter import *
from random import *
from settings import *

VERIFY = 1

def create_halver(numLines, epsilon):
  assert numLines % 2 == 0

  halver = Sorter(numLines)
  mu = 1. / epsilon - 1

  setA = [i+1 for i in xrange(numLines/2)]
  setB = [i+1 + (numLines/2) for i in xrange(numLines/2)]

  for i in xrange(NUM_MATCHINGS):
    halver.add_stage(random_bipartite_stage(numLines, setA, setB))
  
  return halver
    
def random_bipartite_stage(numLines, setA, setB):
  bc = Comparator()
  stage = []
  shuffle(setA)
  shuffle(setB)
  for i in xrange(0,numLines/2):
    stage.append((setA[i],setB[i],bc))
  stage = tuple(stage)
  return stage
