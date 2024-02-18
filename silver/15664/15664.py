def DFS(n, result, idx=-1):
    if n == M:
        if result not in res:
            print(*result)
            res.add(result)
        return
    
    for i in range(idx+1, N):
        DFS(n+1, result+(num_list[i],), i)


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

res = set()
DFS(0, ())