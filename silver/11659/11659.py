import sys
input = sys.stdin.readline


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
dp_array = [0]
for i in range(N):
    dp_array.append(dp_array[-1] + num_list[i])

for _ in range(M):
    s, e = map(int, input().split())
    print(dp_array[e] - dp_array[s-1])