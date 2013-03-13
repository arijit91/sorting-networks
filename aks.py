import sys
import random, separator
import utils

ARGS_NEEDED = 1
USAGE_STRING = 'python aks.py'
RAND_RANGE = 10

d, n, t, alpha, omega = 0, 0, 0, 0, 0
state = {}

eps_b = 0.1
eps_f = 0.01

def init():
    global d, n, t, alpha, omega, state

    argc = len(sys.argv)
    if argc != ARGS_NEEDED:
        print "Usage: ", USAGE_STRING

    d = 12
    n = 2**d
    t = 0
    alpha, omega = 0, 0

    inputs = range(1, n+1)
    random.shuffle(inputs)

    state[0] = [(i + 1, inputs[i]) for i in xrange(n)]
    #state[0] = [(i + 1, random.randint(1, 10)) for i in xrange(n)]

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

def get_level(node):
    level = 0
    tot = 0
    mul = 2

    while 1:
        if tot >= node:
            return level
        tot += mul
        mul *= 2
        level += 1

    return level

def c(i, t):
    return n * 2 ** (2 * i - t - 2)

def get_outputs_for_node(node):
    global d, n, t, alpha, omega, state
    outputs = []

    level = get_level(node)

    if t == 0: # Send one half to each child
        wire_val_list = state[node]
        num_wires = len(wire_val_list)
        
        assert num_wires == n
        s = separator.Separator(num_wires, 0, eps_b, eps_f)

        return s.separate(wire_val_list)

    if t == 1:
        wire_val_list = state[node]
        
        num_wires = len(wire_val_list)
        assert num_wires == n / 2
        assert n % 32 == 0

        s = separator.Separator(num_wires, num_wires / 16, eps_b, eps_f)

        return s.separate(wire_val_list)

    else:
        wire_val_list = state[node]
        num_wires = len(wire_val_list)

        if level == get_alpha(t) and level + 1 == get_alpha(t+1) :
            assert num_wires == c(level, t)
            s = separator.Separator(num_wires, 0, eps_b, eps_f)

        elif level == get_alpha(t) and level - 1 == get_alpha(t+1) :
            assert num_wires == c(level, t)
            assert num_wires % 16 == 0
            s = separator.Separator(num_wires, num_wires / 16, eps_b, eps_f)

        elif alpha < level < omega and level % 2 == t % 2 :
            assert num_wires * 64 == 63 * c(level, t)
            assert num_wires % 21 == 0
            s = separator.Separator(num_wires, num_wires / 21, eps_b, eps_f)

        elif level == omega and t % 3 == 1 :
            assert num_wires * 64 == 63 * c(level, t)
            assert num_wires % 21 == 0
            s = separator.Separator(num_wires, num_wires / 21, eps_b, eps_f)

        elif level == omega and t % 3 == 2 :
            assert num_wires * 64 == 15 * c(level, t)
            assert num_wires % 5 == 0
            s = separator.Separator(num_wires, num_wires / 5, eps_b, eps_f)

        else:
            assert num_wires * 64 == 3 * c(level, t)
            assert level == omega and t % 3 == 0
            s = separator.Separator(num_wires, num_wires, eps_b, eps_f)

        return s.separate(wire_val_list)
        
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

def get_alpha(time):
    if 0 <= time <= d - 5:
        return (time % 2)
    elif time % 4 == 1:
        return (time - d + 5) / 2
    elif time % 4 == 2:
        return (time - d + 6) / 2
    elif time % 4 == 3:
        return (time - d + 7) / 2
    else:
        return (time - d + 8) / 2

def get_omega(time):
    if t == 0:
        return 0
    elif t % 3 == 1:
        return (t + 2) / 3
    elif t % 3 == 2:
        return (t + 4) / 3
    else:
        return (t + 6) / 3
    
def update_alpha():
    global d, n, t, alpha, omega, state
    alpha = get_alpha(t)

def update_omega():
    global d, n, t, alpha, omega, state
    omega = get_omega(t)

def update_vars():
    update_alpha()
    update_omega()

def main():
    global d, n, t, alpha, omega, state

    init()

    while t <= (3 * d - 21):

        #for key in state.keys():
        #    print key, get_level(key)
        #    print state[key]

        stats()
        
        get_next_state()

        t += 1

        update_vars()

        #val = raw_input()

    stats()
    #for key in state.keys():
    #    print key, get_level(key)
    #    print state[key]

    outputs = []
    for key in state.keys():
        vals = [y for (x, y) in state[key]]
        vals.sort()
        outputs.extend(vals)

    print "Output:"
    print outputs

    print utils.inversionCount(outputs)

main()
