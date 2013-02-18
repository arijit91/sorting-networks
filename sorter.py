import sys
import comparator
import itertools
import utils

class Sorter():
    def __init__(self, numLines):
        self.stages = []
        self.numStages = 0

        self.numLines = numLines
        
        self.inputs = []
        self.lineVals = []
        self.outputs = []

    def verify(self, stage):
        s = set()
        cnt = 0
        for elem in stage:
            for x in elem[:-1]:
                if (self.numLines >= x >= 1):
                    s.add(x)
                    cnt += 1
                else:
                    sys.stderr.write("Stage: Out of bounds\n")
                    return False

        if len(s) != cnt:
            sys.stderr.write("Stage: Duplication found\n")
            return False

        return True

    def disp(self):
      for index, stage in enumerate(self.stages):
        print "Stage %d:" % index
        for elem in stage:
          print elem[0], elem[1], elem[2]
        print

    def add_stage(self, stage, verify = 0, index = -1):
        if (verify):
            if not self.verify(stage):
                sys.stderr.write("Bad stage. Not adding stage...\n")
                return

        self.numStages += 1

        if (index != -1):
            self.stages.insert(index, stage)
        else :
            self.stages.append(stage)

    def set_all_comparators(self, comp):
      for stage in self.stages:
        for elem in stage:
          elem[2] = comp

    def comparator_swap(self):
      bc = comparator.Comparator()
      rev = comparator.ReverseComparator()
      for stage in self.stages:
        for elem in stage:
          name = elem[2].__class__.__name__
          assert name == "Comparator" or name == "ReverseComparator"
          if name == "Comparator":
            elem[2] = rev
          else:
            elem[2] = bc

    def simulate(self, step):
        curInput = self.lineVals[-1]
        curOutput = curInput

        stage = self.stages[step]

        for elem in stage:
            lo = min(elem[0], elem[1]) - 1
            hi = max(elem[0], elem[1]) - 1

            out = elem[2].output((curInput[lo], curInput[hi]))

            curOutput[lo], curOutput[hi] = out

        self.lineVals.append(curOutput)

        
    def sort(self, inputs):
        self.inputs = inputs
        self.lineVals = [self.inputs]

        for i in xrange(self.numStages):
            self.simulate(i)

        self.outputs = self.lineVals[-1]
        return self.outputs

    def does_it_sort(self):
        bad = False
        for i in xrange(1<<(self.numLines)):
            if bad:
                break
            inputs = []
            for j in xrange(self.numLines):
                inputs.append((i>>j)&1)
            out = self.sort(inputs)
            for i in xrange(1, self.numLines):
                if out[i-1] == 1 and out[i] == 0 : 
                    print "Sorting Network fails on input: "
                    print inputs
                    print out
                    bad = True
                    break
        if not bad:
            print "You got yourself a valid Sorting Network!"

    # One above another
    def combine(self, sorter):
      for stage in sorter.stages:
        for elem in stage:
          elem[0] += self.numLines
          elem[1] += self.numLines

      self.numLines += sorter.numLines

      for i in xrange(sorter.numStages):
          if i < self.numStages:
            self.stages[i].extend(sorter.stages[i])

          else :
            self.stages.append(sorter.stages[i])

      for stage in self.stages:
        self.verify(stage)

    # One after another
    def join(self, sorter):
      assert self.numLines == sorter.numLines

      self.numStages += sorter.numStages
      self.stages.extend(sorter.stages)

    def render(self, matrix):
      for row in matrix:
        for char in row:
          print char,
        print

    def get_inversions_rating(self):
      rating_sum = count = 0
      for perm in itertools.permutations(range(self.numLines)):
        inputs = list(perm)
        out = self.sort(inputs)
        rating_sum += utils.inversionCount(out)
        count += 1
      rating = rating_sum / float(count)
      return rating

    def get_maxinv_rating(self):
      rating = -1
      maxseq = []
      for perm in itertools.permutations(range(self.numLines)):
        inputs = list(perm)
        out = self.sort(inputs)
        new_rating = utils.inversionCount(out)
        if rating < new_rating:
          rating = new_rating
          maxseq = inputs
      return (rating, maxseq)
      

    def display_ascii_art(self):
      width, height = 1, 2 * self.numLines
      for stage in self.stages:
        width += len(stage)
      width += 2*len(self.stages)
      zigzag = [ "\\" , "/" ]
     
      dispOutput = [['_' for j in xrange(width)] for i in xrange(height)]

      for index in xrange(1, height, 2):
          dispOutput[index] = [' ' for j in xrange(width)]
    
      
      xpos = 1
      for stage in self.stages:
        for elem in stage:
          lo = min(elem[0], elem[1]) - 1
          hi = max(elem[0], elem[1]) - 1

          for row in xrange(2*lo + 1, 2*hi + 1):
            dispOutput[row][xpos] = '|'
            if row == 2*lo+1 and elem[2].__class__.__name__ == "Comparator":
                dispOutput[row][xpos] = '^'

            if row == 2*hi and \
                elem[2].__class__.__name__ == "ReverseComparator":

                dispOutput[row][xpos] = 'v'
            
            if elem[2].__class__.__name__ == "FaultyComparator":

                dispOutput[row][xpos] = zigzag[row % 2]

          xpos += 1

        xpos += 2
      #dispOutput[1][1] = '|'
      #dispOutput[2][1] = '|'

      #dispOutput[1][3] = '|'
      #dispOutput[2][3] = '|'
      #dispOutput[3][3] = '|'
      #dispOutput[4][3] = '|'

      self.render(dispOutput)
