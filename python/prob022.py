with open('p022_names.txt') as f:
    l = f.read().split(',')
    l.sort()

f = lambda i, n: i * sum([ord(x)-64 for x in n])
print sum([f(l.index(n)+1, n.split("\"")[1]) for n in l])
