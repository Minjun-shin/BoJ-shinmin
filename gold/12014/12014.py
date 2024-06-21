def binsearch(num):
    s, e = 0, K
    while s <= e:
        middle = (s + e) // 2
        if dp[middle] < num:
            s = middle + 1
        
        else:
            e = middle - 1
    
    return s


T = int(input())

for test_case in range(1, T+1):
    print(f'Case #{test_case}')
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    dp = [0] + [float('inf')] * K
    
    for num in num_list:
        dp[binsearch(num)] = num
        if dp[-1] != float('inf'): break
    
    print(1 if dp[-1] != float('inf') else 0)