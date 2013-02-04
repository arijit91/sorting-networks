class BaseComparator():
    def __init__(self, a, b):
        self.input = (a, b)

    def output(self):
        if self.input[0] <= self.input[1]:
            return (self.input[0], self.input[1])
        else :
            return (self.input[1], self.input[0])

class ReverseComparator(BaseComparator):
    def output(self):
        if self.input[0] > self.input[1]:
            return (self.input[0], self.input[1])
        else :
            return (self.input[1], self.input[0])
