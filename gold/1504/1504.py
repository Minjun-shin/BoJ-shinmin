from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra(start):
    dists = [float('inf')] * N
    dists[start] = 0
    pQ = [(0, start)]

    while pQ:
        dist, curr = heappop(pQ)

        if dist > dists[curr]:
            continue

        for i, w in graphs[curr]:
            if dists[i] > dist + w:
                dists[i] = dist + w
                heappush(pQ, (dists[i], i))
    
    return dists



N, M = map(int, input().split())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

v1, v2 = map(int, input().split())
d = dijkstra(v1-1)[v2-1]
dists1 = dijkstra(0)
dists2 = dijkstra(N-1)

res = d + min(dists1[v1-1] + dists2[v2-1], dists1[v2-1] + dists2[v1-1])

print(res if res != float('inf') else -1)