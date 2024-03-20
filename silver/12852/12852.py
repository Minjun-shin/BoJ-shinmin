from collections import deque


N = int(input())
res = [[float('inf'), []] for _ in range(N+1)]
res[N] = [0, [N]]
dQ = deque()
dQ.append(N)

while dQ and res[1][0] == float('inf'):
    i = dQ.popleft()
    if i-1 > 0 and res[i-1][0] == float('inf'):
        res[i-1] = [res[i][0] + 1, res[i][1] + [i-1]]
        dQ.append(i-1)

    if i % 2 == 0 and res[i//2][0] == float('inf'):
        res[i//2] = [res[i][0] + 1, res[i][1] + [i//2]]
        dQ.append(i//2)

    if i % 3 == 0 and res[i//3][0] == float('inf'):
        res[i//3] = [res[i][0] + 1, res[i][1] + [i//3]]
        dQ.append(i//3)

print(res[1][0])
print(*res[1][1])