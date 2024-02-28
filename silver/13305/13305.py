N = int(input())
dists = list(map(int, input().split()))
oils = list(map(int, input().split()))

res = 0
oil = oils[0]
for i in range(N-1):
    oil = min(oil, oils[i])
    res += oil * dists[i]

print(res)