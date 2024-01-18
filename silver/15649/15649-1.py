def DFS(n, res):
    if n == M:
        result.append(res)
    for i in range(1, N+1):
        if ch[i] == 0:
            ch[i] = 1
            DFS(n+1, res + [i])
            ch[i] = 0
    

N, M = map(int, input().split())
ch = [0] * (N + 1)
result = []
DFS(0, [])
for nums in result:
    print(*nums)