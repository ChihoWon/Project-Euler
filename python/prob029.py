limit = 100
s = set();
for x in range(2, limit + 1):
    for y in range(2, limit + 1):
        s.add(x**y)

print len(s)
