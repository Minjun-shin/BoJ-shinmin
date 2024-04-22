import sys
input = sys.stdin.readline


N = int(input())
num_list = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    if i > 0 and num_list[i-1] == num_list[i]:
        dp[i-1][i] = 1

for i in range(2, N):
    for j in range(N-i):
        if num_list[j] == num_list[j+i]:
            dp[j][j+i] = dp[j+1][j+i-1]

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])