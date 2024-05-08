import sys
input = sys.stdin.readline


N = int(input())
num_list = [int(input()) for _ in range(N)]

dp = [[0] * 3 for _ in range(N+1)]
dp[1][0], dp[1][1], dp[1][2] = 0, num_list[0], num_list[0]

for i in range(2, N+1):
    dp[i][0], dp[i][1], dp[i][2] = max(dp[i-1]), max(dp[i-2]) + num_list[i-1], dp[i-1][1] + num_list[i-1]

print(max(dp[-1]))