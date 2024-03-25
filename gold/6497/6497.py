from heapq import heappop, heappush
import sys
input = sys.stdin.readline


while True:
    N, M = map(int, input().split())
    if N == M == 0:
         break
    graphs = [[] for _ in range(N)]
    total = 0

    for _ in range(M):
        s, e, w = map(int, input().split())
        total += w
        graphs[s].append((e, w))
        graphs[e].append((s, w))

    pQ = []
    heappush(pQ, (0, 0))
    visited = [0] * N
    res = 0

    while pQ:
        weight, curr = heappop(pQ)

        if visited[curr] == 1:
            continue

        visited[curr] = 1
        res += weight

        for i, w in graphs[curr]:
            if visited[i] == 0:
                    heappush(pQ, (w, i))

    print(total - res)