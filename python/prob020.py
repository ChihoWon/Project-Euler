r = 1
i = 100

while i > 1:
    r *= i
    i -= 1

print sum([int(x) for x in str(r)])
