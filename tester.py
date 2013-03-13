import separator
import random
import halver

eps_b = 0.01
eps_f = 0.001

n = 1000
f = 50
x = range(n)
random.shuffle(x)

s = separator.Separator(n, f, eps_b, eps_f)

#print x
par, lc, rc = s.separate(zip(range(n), x))

print par
print
print lc
print
print rc

#h = halver.create_halver(100, eps_b)
#
#x = range(100)
#random.shuffle(x)
#
#print x
#print h.sort(x)
#
#bad = [elem for elem in x[:50] if elem > 50]
#
#print bad
