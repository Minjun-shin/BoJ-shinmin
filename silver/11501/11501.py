T = int(input())
 
for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    res = 0
    max_value = 0
    for i in range(N-1, -1, -1):
        if num_list[i] > max_value:
            max_value = num_list[i]

        else:
            res += max_value - num_list[i]

    print(res)