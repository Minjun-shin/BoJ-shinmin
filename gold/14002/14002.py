N = int(input())
num_list = list(map(int, input().split()))

dp = [[num_list[i]] for i in range(N)]
dp[0] = [num_list[0]]
res = []

for i in range(1, N):
    for j in range(i):
        if num_list[i] > dp[j][-1] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [num_list[i]]

for i in range(N):
    if len(res) < len(dp[i]):
        res = dp[i]
        
print(len(res))
print(*res)