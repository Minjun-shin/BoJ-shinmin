N, K = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

dp = [float('inf')] * (K + 1)
dp[0] = 0

for i in range(1, K+1):
    for num in num_list:
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i-num]+1)

print(-1 if dp[-1] == float('inf') else dp[-1])