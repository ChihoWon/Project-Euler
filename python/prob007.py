from math import sqrt

def Sieve_of_Eratosthenes(n):
    sieve = range(n + 1)
    sieve[1] = 0
    rn = int(round(sqrt(n)))
    for x in range(2, rn + 1):
        if sieve[x]:
            sieve[x*x:n+1:x] = [0] * len(sieve[x*x:n+1:x])
    return filter(lambda x: x != 0, sieve)

l = Sieve_of_Eratosthenes(200000)
print l[10000]
