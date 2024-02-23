from collections import deque


N, M = map(int, input().split())
res = []
table = deque(range(1, N+1))

while table:
    table.rotate(-M)
    res.append(table.pop())

print('<', end='')
print(*res, sep=', ', end='')
print('>')