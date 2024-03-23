from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M = int(input()), int(input())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    if s == e:
        continue

    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

pQ = []
heappush(pQ, (0, 0))
visited = [0] * N
total = 0

while pQ:
    weight, curr = heappop(pQ)

    if visited[curr] == 1:
        continue

    total += weight
    visited[curr] = 1

    for i, w in graphs[curr]:
        if visited[i] == 0:
            heappush(pQ, (w, i))

print(total)