from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
connects = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    connects[s-1].append(e-1)
    connects[e-1].append(s-1)

dists = [float('inf')] * N
dists[0] = 0

dQ = deque()
dQ.append(0)
while dQ:
    curr = dQ.popleft()
    for i in connects[curr]:
        if dists[i] == float('inf'):
            dists[i] = dists[curr] + 1
            dQ.append(i)

res = [0, 0, 0]
for idx in range(N):
    if dists[idx] > res[1]:
        res[0] = idx + 1
        res[1] = dists[idx]
        res[2] = 1
    elif dists[idx] == res[1]:
        res[2] += 1

print(*res)