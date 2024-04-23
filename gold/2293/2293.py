N, K = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for num in num_list:
    for i in range(1, K+1):
        if i-num >= 0:
            dp[i] += dp[i-num]

print(dp[-1])