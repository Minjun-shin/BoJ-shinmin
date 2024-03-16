import heapq
import sys
input = sys.stdin.readline


N = int(input())
hQ = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if hQ:
            res1, res2 = heapq.heappop(hQ)
            print(res2)

        else:
            print(0)

    else:
        heapq.heappush(hQ, (abs(num), num))