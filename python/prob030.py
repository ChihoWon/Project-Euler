def pe30(n):
    ret = 0
    for i in str(n):
        ret += int(i) ** 5
    return ret

l = list()

for x in range(1000, 9**5*4):
    if x == pe30(x):
        l.append(x)

print sum(l)
