class Comparator():
    def output(self, inputs):
        if inputs[0] <= inputs[1]:
            return (inputs[0], inputs[1])
        else :
            return (inputs[1], inputs[0])
