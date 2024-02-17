def DFS(n, result):
    if n == M:
        print(*result)
        return
    
    for i in range(N):
        DFS(n+1, result + [num_list[i]])


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

DFS(0, [])