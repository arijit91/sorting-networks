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

    d = 12
    n = 2**d
    t = 0
    alpha, omega = 0, 0

    state[0] = [(i + 1, random.randint(1, RAND_RANGE)) for i in xrange(n)]

def stats():
    global d, n, t, alpha, omega, state

    print "Stats at t = %d" % t

    #print "State:"
    #print state
    #print 

    print "Wire counts:"
    counts = [(node, len(state[node])) for node in state.keys()]
    print counts
    print 

def get_outputs_for_node(node):
    global d, n, t, alpha, omega, state
    outputs = []

    if t == 0: # Send one half to each child
        wire_val_list = state[node]
        
        assert len(wire_val_list) == n
        outputs.append([])
        outputs.append(wire_val_list[:n/2])
        outputs.append(wire_val_list[n/2:])

        return outputs

    if t == 1:
        wire_val_list = state[node]
        
        num_wires = len(wire_val_list)
        assert num_wires == n / 2
        assert n % 32 == 0

        sx = n / 32
        sy = (n / 2 - sx) / 2 + sx

        outputs.append(wire_val_list[:sx])
        outputs.append(wire_val_list[sx:sy])
        outputs.append(wire_val_list[sy:])

        return outputs

    return [], [], []
        
def get_next_state():
    global d, n, t, alpha, omega, state

    next_state = {}
    for node in state.keys():
        outputs = get_outputs_for_node(node)

        neighbours = [(node - 1)/2, 2 * node + 1, 2 * node + 2]

        for index, neighbour in enumerate(neighbours):
            if neighbour in next_state.keys():
                next_state[neighbour].extend(outputs[index])
            elif outputs[index]:
                next_state[neighbour] = outputs[index]

    state = next_state

    print "Generating next state..."

def update_alpha():
    global d, n, t, alpha, omega, state

    if 0 <= t <= d - 5:
        alpha = (t % 2)
    elif t % 4 == 1:
        alpha = (t - d + 5) / 2
    elif t % 4 == 2:
        alpha = (t - d + 6) / 2
    elif t % 4 == 3:
        alpha = (t - d + 7) / 2
    else:
        alpha = (t - d + 8) / 2

def update_omega():
    global d, n, t, alpha, omega, state

    if t == 0:
        omega = 0
    elif t % 3 == 1:
        omega = (t + 2) / 3
    elif t % 3 == 2:
        omega = (t + 4) / 3
    else:
        omega = (t + 6) / 3
    

def update_vars():
    update_alpha()
    update_omega()

def main():
    global d, n, t, alpha, omega, state

    init()

    while t <= (3 * d - 5):
        stats()
        
        get_next_state()

        t += 1

        update_vars()

        val = raw_input()

    stats()


main()
