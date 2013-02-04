import sys
import comparator

class Sorter():
    def __init__(self, inputs):
        self.stages = []
        self.numStages = 0

        self.inputs = inputs
        self.numLines = len(self.inputs)
        
        self.lineVals = []
        self.outputs = []

    def verify(self, stage):
        print stage
        s = set()
        cnt = 0
        for elem in stage:
            for x in elem:
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

    def simulate(step):

        
    def sort(self):
        self.lineVals = [self.inputs]

        for i in xrange(self.numStages):
            self.simulate(i):

        self.outputs = self.lineVals[-1]
        print self.outputs
