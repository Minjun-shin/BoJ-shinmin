import sys
input = sys.stdin.readline


N, M = map(int, input().split())
ch = {input().strip() for _ in range(N)}

res = 0
for _ in range(M):
    if input().strip() in ch:
        res += 1

print(res)