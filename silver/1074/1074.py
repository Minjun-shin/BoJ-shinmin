N, r, c = map(int, input().split())
middle = 2 ** (N-1)
res = ''

while middle >= 1:
    tmp = 0
    if r >= middle:
        tmp += 2
        r -= middle

    if c >= middle:
        tmp += 1
        c -= middle

    res += str(tmp)
    middle //= 2

print(int(res, 4))