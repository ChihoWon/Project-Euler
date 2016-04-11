def f1(a, b):
    while b:
        a, b = b, a % b
    return a

def f2(a,b=1):
    c = 1
    while True:
        c = (c**2 + b) % a
        yield c

def f3(a, b=1000, c=10):
    d = f2(a)
    e = f2(a)
    f = 0
    g = 1
    while True:
        while f<b:
            h = d.next()
            e.next()
            i = e.next()
            f += 1
            j = abs(i-h)
            if not j: continue
        d = f1(j,a)
        if a > d > 1:
            return f3(d) + f3(a//d)
        if g<c:
            g+=1
            d = f2(a,g)
            e = f2(a,g)
            f = 0
        else:
            break
    return [a]

print sorted(f3(600851475143))
print max(f3(600851475143))
