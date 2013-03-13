from comparator import *
from sorter import *
from random import *

VERIFY = 1

def create_halver(numLines, epsilon):
  assert numLines % 2 == 0

  halver = Sorter(numLines)
  mu = 1. / epsilon - 1
  d = 10 #something gen for now
  for i in range(0,d):
    halver.add_stage(random_bipartite_stage(numLines), VERIFY)
  
  return halver
    
def random_bipartite_stage(numLines):
  bc = Comparator()
  stage = []
  setA = [i+1 for i in range(0,numLines/2)]
  setB = [i+1 + (numLines/2) for i in range(0,numLines/2)]
  shuffle(setA)
  shuffle(setB)
  #print setA
  #print setB
  for i in range(0,numLines/2):
    stage.append((setA[i],setB[i],bc))
  stage = tuple(stage)
  #print stage
  return stage
