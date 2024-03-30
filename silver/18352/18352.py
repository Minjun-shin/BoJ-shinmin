from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graphs[s-1].append(e-1)

pQ = []
dists = [float('inf')] * N
dists[X-1] = 0
heappush(pQ, (0, X-1))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists[curr]:
        continue

    for i in graphs[curr]:
        if dists[i] > dist + 1:
            dists[i] = dist + 1
            heappush(pQ, (dists[i], i))

res = []
for idx in range(N):
    if dists[idx] == K:
        res.append(idx + 1)

if res:
    print(*res, sep='\n')
else:
    print(-1)