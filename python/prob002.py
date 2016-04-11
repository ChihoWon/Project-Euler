a = 1
b = 2
s = 0

while b <= 4000000:
    if b % 2 is 0:
        s += b
    a, b = b, a + b

print s
