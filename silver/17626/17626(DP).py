import math


N = int(input())
res = [0] * (N+1)
res[1] = 1

for i in range(2, N+1):
    tmp = 4
    for j in range(1, int(math.sqrt(i))+1):
        tmp = min(tmp-1, res[i-j**2]) + 1
    res[i] = tmp

print(res[N])