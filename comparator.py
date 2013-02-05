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
