import heapq
import sys
input = sys.stdin.readline


N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort()
res = []

for s, t in classes:
    if not res:
        res.append(t)
        continue

    if s >= res[0]:
        heapq.heappop(res)

    heapq.heappush(res, t)

print(len(res))