from sys import *
from sorter import *
from comparator import *
from random import *

VERIFY = 1

def create_halver(numLines, epsilon):
    
  halver = Sorter(numLines)
  mu = 1 / epsilon
  d = 5 #something
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
  print setA
  print setB
  for i in range(0,numLines/2):
    stage.append((setA[i],setB[i],bc))
  stage = tuple(stage)
  print stage
  return stage
    
halver = create_halver(20, 0.1)
halver.display_ascii_art()

