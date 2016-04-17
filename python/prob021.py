from math import sqrt

def d(n):
    ret = set()
    for x in range(1, int(sqrt(n)) + 1):
        if not n % x:
            ret.add(x)
            ret.add(n//x)
    ret.remove(n)
    return sum(ret)

ans = 0
for i in range(2, 10000):
    b = d(i)
    a = d(b)
    if i == a and i != b:
        ans += i

print ans
