def is_palindromic(n):
    return str(n) == str(n)[::-1]

ans = 0

for x in range(1, 1000000):
    if is_palindromic(x) and is_palindromic(bin(x)[2:]):
        ans += x

print ans
