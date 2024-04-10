N = int(input())
dp = [0] * (N + 1)
if N >= 2:
    dp[0] = 1
    dp[2] = 3

for i in range(4, N+1, 2):
    tmp = dp[i-2]
    for j in range(0, i, 2):
        tmp += dp[j] * 2
    dp[i] = tmp

print(dp[-1])