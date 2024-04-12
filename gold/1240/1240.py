from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra(start, goal):
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

    return dists[goal]


N, M = map(int, input().split())
graphs = [[] for _ in range(N)]

for _ in range(N-1):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

for _ in range(M):
    s, e = map(int, input().split())
    print(dijkstra(s-1, e-1))