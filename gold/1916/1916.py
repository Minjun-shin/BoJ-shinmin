import heapq
import sys
input = sys.stdin.readline


N, M = int(input()), int(input())
board = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    board[s-1].append((e-1, w))

start, end = map(int, input().split())
dists = [float('inf')] * N
dists[start-1] = 0

pQ = []
heapq.heappush(pQ, (0, start-1))

while pQ:
    dist, curr = heapq.heappop(pQ)

    if dist > dists[curr] or curr == end - 1:
        continue

    for idx, weight in board[curr]:
        if dists[idx] > dist + weight:
            dists[idx] = dist + weight
            heapq.heappush(pQ, (dists[idx], idx))

print(dists[end-1])