from math import factorial as fact

l = [fact(x) for x in range(0, 10)]
ans = 0

for x in range(3, 100000):
    t = x
    s = 0
    while t != 0:
        s += l[t % 10]
        t //= 10
    if s == x:
        ans += x

print ans
