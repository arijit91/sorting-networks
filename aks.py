import sys
import random

ARGS_NEEDED = 1
USAGE_STRING = 'python aks.py'
RAND_RANGE = 10

d, n, t, alpha, omega = 0, 0, 0, 0, 0
state = {}

def init():
    global d, n, t, alpha, omega, state

    argc = len(sys.argv)
    if argc != ARGS_NEEDED:
        print "Usage: ", USAGE_STRING

    d = 8
    n = 2**d
    t = 0
    alpha, omega = 0, 0

    state[0] = [(i + 1, random.randint(1, RAND_RANGE)) for i in xrange(n)]

def stats():
    global d, n, t, alpha, omega, state

    print "Stats at t = %d" % t

    print "State:"
    print state
    print 

    print "Wire counts:"
    counts = [(node, len(state[node])) for node in state.keys()]
    print counts
    print 

def get_component_at_time(node):
    pass

def apply_component_on_node(comp, node):
    return [], [], []


def get_next_state():
    global d, n, t, alpha, omega, state

    next_state = {}
    for node in state.keys():
        comp = get_component_at_time(node)
        outputs = apply_component_on_node(comp, node)

        neighbours = [node / 2, 2 * node + 1, 2 * node + 2]

        for index, neighbour in enumerate(neighbours):
            if neighbour in next_state.keys():
                next_state[neighbour].extend(outputs[index])
            elif outputs[index]:
                next_state[neighbour] = outputs[index]

    state = next_state

    print "Generating next state..."

def main():
    global d, n, t, alpha, omega, state

    init()

    while t <= (3 * d - 5):
        stats()
        
        get_next_state()

        t += 1

        val = raw_input()

    stats()


main()
