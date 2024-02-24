N = int(input())
res = [0] * (N+1)

for i in range(N):
    day, val = map(int, input().split())
    for j in range(i+day, N+1):
        res[j] = max(res[j], res[i] + val)

print(res[-1])