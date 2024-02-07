import sys
input = sys.stdin.readline


N = int(input())
res = [tuple(map(int, input().split())) for _ in range(N)]
res.sort()

for corr in res:
    print(*corr)