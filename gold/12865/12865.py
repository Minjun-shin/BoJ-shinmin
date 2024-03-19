N, K = map(int, input().split())
dp = [0] * (K+1)

for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K-w, -1, -1):
        dp[i+w] = max(dp[i+w], dp[i] + v)

print(max(dp))