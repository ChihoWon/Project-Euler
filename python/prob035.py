from math import sqrt
from math import log10

def Sieve_of_Eratosthenes(n):
    sieve = range(n + 1)
    sieve[1] = 0
    rn = int(round(sqrt(n)))
    for x in range(2, rn + 1):
        if sieve[x]:
            sieve[x*x:n+1:x] = [0] * len(sieve[x*x:n+1:x])
    return filter(lambda x: x != 0, sieve)

l = Sieve_of_Eratosthenes(1000000)
count = 0

def check_circular(n):
    for x in range(1, int(log10(int(n))) + 1):
        if not int(n[x:] + n[:x]) in l:
            return False
    return True

for x in l:
    if check_circular(str(x)):
        count += 1

print count
