def DFS(n, result):
    if n == M:
        print(*result)
        return
    
    for i in range(N):
        if ch[i] == 0:
            ch[i] = 1
            DFS(n+1, result+[num_list[i]])
            ch[i] = 0


N, M = map(int, input().split())
ch = [0] * N
num_list = list(map(int, input().split()))
num_list.sort()
DFS(0, [])