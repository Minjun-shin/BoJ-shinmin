N = int(input())
num_list = list(map(int, input().split()))
res = [0] * N
res[0] = 1

for i in range(1, N):
    tmp = 0
    for j in range(i):
        if num_list[j] < num_list[i]:
            tmp = max(tmp, res[j])
    
    res[i] = tmp + 1

print(max(res))