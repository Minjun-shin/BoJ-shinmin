def DFS(n, result):
    if n == M:
        res.append(result)
        return
    
    for i in range(result[-1] if result else 1, N+1):
        DFS(n+1, result+[i])


N, M = map(int, input().split())
res = []
DFS(0, [])

for nums in res:
    print(*nums)