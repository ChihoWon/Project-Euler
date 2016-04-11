def Collatz_cycle(n):
    ret = 0
    while n-1:
        if n < 1: return ret
        ret += 1
        if not n & 1:
            n >>= 1
        else:
            n = 3 * n + 1
    return ret + 1

a = 0
r = 0
for x in range(1, 1000000):
    c = Collatz_cycle(x)
    if c > r:
        a = x
        r = c

print a, r
