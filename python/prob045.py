P = lambda n: n*(3*n-1)/2
H = lambda n: n*(2*n-1)

N = 100000

a = set([P(n) for n in range(1, N)])
b = set([H(n) for n in range(1, N)])

print sorted(a & b)
