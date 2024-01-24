N = int(input())
res = [0] * (N+1)

for i in range(2, N+1):
    tmp = res[i-1]

    if i % 3 == 0:
        tmp = min(tmp, res[i // 3])

    if i % 2 == 0:
        tmp = min(tmp, res[i // 2])

    res[i] = 1 + tmp

print(res[-1])