N = int(input())

res = [[0, 0] for _ in range(N+1)]
res[1] = [1, 0]

for i in range(2, N+1):
    res[i] = [res[i-1][1], sum(res[i-1])]

print(sum(res[-1]))