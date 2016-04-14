l = []
for x in range(1, 1001):
    l.append(x**x)
L = len(str(sum(l)))
print str(sum(l))[L-10:L]
