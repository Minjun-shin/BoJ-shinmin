def DFS(n, total=0):
    global res
    if n > N:
        return
    res = max(res, total)
    
    for i in range(n, N):
        day, price = days[i]
        DFS(i+day, total+price)


N = int(input())
days = [tuple(map(int, input().split())) for _ in range(N)]

res = 0
DFS(0)
print(res)