l = [1]
s = 1
N = 1001
t = 0
r = 0

while s < N * N:
    if not r % 4:
        t += 2
    s += t
    l.append(s)
    r += 1

print sum(l)
