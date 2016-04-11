def f(n):
    a, b = 1, 1
    while a < n:
        b = 1
        while b < n - a:
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
            b += 1
        a += 1

print f(1000)
