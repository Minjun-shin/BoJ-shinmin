from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N = int(input())
pQ = []
for _ in range(N):
    heappush(pQ, int(input()))

res = 0

while len(pQ) > 1:
    num1 = heappop(pQ)
    num2 = heappop(pQ)
    res += num1 + num2
    heappush(pQ, num1 + num2)

print(res)