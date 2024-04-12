from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S, E = map(int, input().split())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

res = float('inf')
visited = [0] * N
pQ = [(-float('inf'), S-1)]
status = False

while pQ:
    weight, curr = heappop(pQ)

    if visited[curr] == 1:
        continue

    visited[curr] = 1
    res = min(res, -weight)

    if visited[E-1] == 1:
        break

    for i, w in graphs[curr]:
        if visited[i] == 0:
            heappush(pQ, (-w, i))

else:
    status = True
    
if status:
    print(0)
else:
    print(res)