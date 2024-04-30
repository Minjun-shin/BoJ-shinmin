N = int(input())
num_list = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(N):
    dp[num_list[i]] = dp[num_list[i]-1] + 1

print(N - max(dp))