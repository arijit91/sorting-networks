f = open('out', 'r')
c = 0
s = 0
for line in f:
    if c % 2 == 0:
        s += int(line)
    c += 1

c = (c + 1) / 2

s /= c
print s
f.close()
