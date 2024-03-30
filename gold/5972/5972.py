from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

dists = [float('inf')] * N
dists[0] = 0
pQ = []
heappush(pQ, (0, 0))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists[curr]:
        continue

    for i, w in graphs[curr]:
        if dists[i] > dist + w:
            dists[i] = dist + w
            heappush(pQ, (dists[i], i))

print(dists[-1])