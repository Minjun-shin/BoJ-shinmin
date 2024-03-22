from heapq import heappop, heappush
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
board = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    board[s-1].append((e-1, w))
    board[e-1].append((s-1, w))

pQ = []
heappush(pQ, (0, 0))
visited = [0] * V
res = 0

while pQ:
    weight, curr = heappop(pQ)

    if visited[curr] == 1:
        continue

    visited[curr] = 1
    res += weight

    for i, w in board[curr]:
        if visited[i] == 0:
            heappush(pQ, (w, i))

print(res)