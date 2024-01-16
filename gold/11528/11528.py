T = int(input())
for _ in range(T):
    test_case, n, m, k = map(int, input().split())
    res = [0] * (n + 1)
    num_list = [m + k * i for i in range((n - m) // k + 1)]
    if m != 1:
        res[1] = 1

    for num in range(2, n+1):
        for i in range(1, num):
            if num - i not in num_list:
                res[num] += res[i]
        
        if num not in num_list:
            res[num] += 1

    print(test_case, res[-1])