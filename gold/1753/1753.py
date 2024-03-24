from heapq import heappop, heappush
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())

checked = set()
graphs = [[] for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))

dists = [float('inf')] * V
dists[K-1] = 0
pQ = []
heappush(pQ, (0, K-1))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists[curr]:
        continue

    for i, w in graphs[curr]:
        if dists[i] > dist + w:
            dists[i] = dist + w
            heappush(pQ, (dists[i], i))

for res in dists:
    if res == float('inf'):
        print('INF')
    else:
        print(res)