import random

class Comparator():
    def output(self, inputs):
        if inputs[0] <= inputs[1]:
            return (inputs[0], inputs[1])
        else :
            return (inputs[1], inputs[0])

    def __str__(self):
      return "Normal Comparator"

class ReverseComparator():
    def output(self, inputs):
        if inputs[0] > inputs[1]:
            return (inputs[0], inputs[1])
        else :
            return (inputs[1], inputs[0])

    def __str__(self):
      return "Reverse Comparator"

class FaultyComparator():
    def __init__(self, prob):
        self.failure_prob = prob

    def output(self, inputs):
      if random.random() >= self.failure_prob:
        if inputs[0] > inputs[1]:
            return (inputs[1], inputs[0])
        else :
            return (inputs[0], inputs[1])
      else :
        return (inputs[0], inputs[1])
        
    def __str__(self):
      return "Faulty Comparator (" + str(self.failure_prob) + ")"
