N = int(input())
num_list = list(map(int, input().split()))
res = 1
tmp1 = 1
tmp2 = 1

for i in range(1, N):
    if num_list[i-1] <= num_list[i]:
        tmp1 += 1

    else:
        res = max(res, tmp1)
        tmp1 = 1

    if num_list[i-1] >= num_list[i]:
        tmp2 += 1

    else:
        res = max(res, tmp2)
        tmp2 = 1

res = max([res, tmp1, tmp2])
print(res)