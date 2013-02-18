import sys
import comparator

class Halver():
  def __init__(self, numLines, epsilon):
    self.numLines = numLines
    self.epsilon = epsilon

    self.stages = []
    
