def is_palindromic(n):
    return str(n) == str(n)[::-1]

def prob004():
    ret = 0
    m = 0
    for i in range(999, 100, -1):
        if i % 11 is 0:
            j = 999
            d = 1
        else:
            j = 990
            d = 11
        while j >= i:
            m = j * i
            if ret > m:
                break
            if is_palindromic(m):
                ret = m
            j -= d
    return ret

print prob004()
