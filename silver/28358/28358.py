T = int(input())
for _ in range(T):
    num_list = list(map(int, input().split()))
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    res = 0
    
    for i in range(12):
        for j in range(days[i]):
            mmdd = list(set(str(i+1) + str(j+1)))
            for num in mmdd:
                if num_list[int(num)]:
                    break
            else:
                res += 1

    print(res)