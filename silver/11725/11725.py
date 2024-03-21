from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N-1):
    s, e = map(int, input().split())
    edges[s-1].append(e-1)
    edges[e-1].append(s-1)

visited = [0] * N
visited[0] = 1
parents = [0] * N

dQ = deque()
dQ.append(0)

while dQ:
    curr = dQ.popleft()

    for num in edges[curr]:
        if visited[num] == 0:
            parents[num] = curr
            visited[num] = 1
            dQ.append(num)

for i in range(1, N):
    print(parents[i] + 1)