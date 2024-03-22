from heapq import heappop, heappush
import sys
input = sys.stdin.readline


V, E, P = map(int, input().split())
graphs = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

pQ = []
dists = [float('inf')] * V
dists[0] = 0
heappush(pQ, (0, 0))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists[curr] or curr == V-1:
        continue

    for i, w in graphs[curr]:
        if dists[i] > dist + w:
            dists[i] = dist + w
            heappush(pQ, (dists[i], i))

dists2 = [float('inf')] * V
dists2[P-1] = 0
heappush(pQ, (0, P-1))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists2[curr] or curr == V-1:
        continue

    for i, w in graphs[curr]:
        if dists2[i] > dist + w:
            dists2[i] = dist + w
            heappush(pQ, (dists2[i], i))

if dists[V-1] == dists[P-1] + dists2[V-1]:
    print("SAVE HIM")

else:
    print("GOOD BYE")