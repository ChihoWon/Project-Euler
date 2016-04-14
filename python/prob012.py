from math import sqrt
trinum = lambda n: n*(n+1)/2

def factors(n):
    ret = set()
    for x in range(1, int(sqrt(n)) + 1):
        if not n % x:
            ret.add(x)
            ret.add(n//x)
    return list(ret)

i = 1
while True:
    if len(factors(trinum(i))) >= 500:
        print trinum(i)
        break
    i += 1
