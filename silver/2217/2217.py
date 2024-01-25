import sys
input = sys.stdin.readline


N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort(reverse=True)

res = 0

for i in range(N):
    rope = num_list.pop()
    res = max(res, rope * (N-i))

print(res)