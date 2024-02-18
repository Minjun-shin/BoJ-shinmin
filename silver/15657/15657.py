def DFS(n, result, idx=0):
    if n == M:
        print(*result)
        return
    
    for i in range(idx, N):
        DFS(n+1, result+[num_list[i]], i)


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

DFS(0, [])