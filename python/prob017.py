s = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # Single
d = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # double
h = 7 # hundred
ans = 0

for n in range(1, 1000):
    x = n / 100 % 10
    y = n / 10 % 10
    z = n % 10

    if x:
        ans += s[x] + h     # hundred
        if y != 0 or z != 0: ans += 3   # and

    if y == 0 or y == 1:
        ans += s[y * 10 + z]    # 1 ~ 19
    else:
        ans += d[y] + s[z]  # 2x ~ 9x

print ans + 11  # final result + 'one thousand'
