T, W = map(int, input().split())

res = [0] * (W+1)

for _ in range(T):
    num = int(input())
    for i in range(W, 0, -1):
        if (num+i) % 2 == 0:
            res[i] = max(res[i], res[i-1])
        else:
            res[i] = max(res[i], res[i-1]) + 1

    if num == 1:
        res[0] += 1

print(max(res))
