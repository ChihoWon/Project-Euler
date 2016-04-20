trees = list()

with open('p067_triangle.txt') as f:
    for line in f:
        trees.append([int(i) for i in line.rstrip('\n').split(" ")])

l = [0 for i in range(len(trees))]
ans = 0

for tree in trees:
    t = 0
    i = 0
    for x in tree:
        p = x
        u = l[i]
        l[i] = p + max(t, l[i])
        t = u
        ans = max(ans, l[i])
        i += 1

print ans
