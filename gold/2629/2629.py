N = int(input())
w_list = list(map(int, input().split()))
M = int(input())
balls = list(map(int, input().split()))
dp = [0] * (max(sum(w_list), max(balls)) * 2 + 1)
middle = len(dp) // 2
dp[middle] = 1

for w in w_list:
    tmp = dp.copy()
    for i in range(len(dp)):
        if i + w < len(dp) and dp[i+w]:
            tmp[i] = 1
        if i - w >= 0 and dp[i-w]:
            tmp[i] = 1
    dp = tmp
print(dp)
for ball in balls:
    print('Y' if dp[ball+middle] else 'N', end=' ')
print()