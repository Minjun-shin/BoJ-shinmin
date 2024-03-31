from heapq import heappop, heappush


def dijkstra(graphs):
    dists = [float('inf')] * N
    dists[X-1] = 0
    pQ = []
    heappush(pQ, (0, X-1))

    while pQ:
        dist, curr = heappop(pQ)

        if dist > dists[curr]:
            continue

        for i, w in graphs[curr]:
            if dists[i] > dist + w:
                dists[i] = dist + w
                heappush(pQ, (dists[i], i))

    return dists


N, M, X = map(int, input().split())
graphs1 = [[] for _ in range(N)]
graphs2 = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graphs1[s-1].append((e-1, w))
    graphs2[e-1].append((s-1, w))

dists1 = dijkstra(graphs1)
dists2 = dijkstra(graphs2)
print(max([dists1[idx] + dists2[idx] for idx in range(N)]))