from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M = int(input()), int(input())
graphs = [[] for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))

S, E = map(int, input().split())
dists = [[float('inf'), []] for _ in range(N)]
dists[S-1] = [0, [S]]
pQ = [(0, S-1, [S])]

while pQ:
    dist, curr, mapping = heappop(pQ)

    if dist > dists[curr][0] or curr == E-1:
        continue

    for i, w in graphs[curr]:
        if dists[i][0] > dist + w:
            dists[i] = [dist + w, mapping + [i+1]]
            heappush(pQ, (dists[i][0], i, dists[i][1]))

print(dists[E-1][0])
print(len(dists[E-1][1]))
print(*dists[E-1][1])