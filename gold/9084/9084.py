T = int(input())

for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    target = int(input())

    dp = [[0] * N for _ in range(target+1)]

    for i in range(1, target+1):
        for j in range(N):
            if i - num_list[j] < 0:
                continue
            tmp = 0
            for k in range(j+1):
                tmp += dp[i - num_list[j]][k]

            if i - num_list[j] == 0:
                dp[i][j] = tmp + 1
            else:
                dp[i][j] = tmp

    print(sum(dp[-1]))