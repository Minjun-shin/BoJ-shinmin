e, s, m = map(int, input().split())

while not (e == s == m):
    if e == min(e, s, m):
        e += 15

    elif s == min(e, s, m):
        s += 28

    else:
        m += 19

print(e)