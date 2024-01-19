def DFS(n, res):
    if n == M:
        result.append(res)
        return

    for i in range(1, N+1):
        DFS(n+1, res + [i])


N, M = map(int, input().split())
result = []
DFS(0, [])
for nums in result:
    print(*nums)