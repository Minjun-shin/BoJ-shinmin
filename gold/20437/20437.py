T = int(input())

for _ in range(T):
    W, K = input(), int(input())
    min_S, max_S = float('inf'), 0
    dp = {chr(i + 97) : [] for i in range(26)}
    for i in range(len(W)):
        dp[W[i]].append(i)
        if len(dp[W[i]]) >= K:
            min_S = min(min_S, dp[W[i]][-1] - dp[W[i]][-1 - K + 1] + 1)
            max_S = max(max_S, dp[W[i]][-1] - dp[W[i]][-1 - K + 1] + 1)
    
    if max_S == 0:
        print(-1)
    else:
        print(min_S, max_S)