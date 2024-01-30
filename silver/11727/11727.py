N = int(input())
res = [0] * (N+1)

res[0], res[1] = 1, 1

for i in range(2, N+1):
    res[i] = res[i-1] + 2 * res[i-2]

print(res[-1] % 10007)