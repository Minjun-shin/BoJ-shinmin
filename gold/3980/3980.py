def DFS(n, result, tmp):
    global res
    if n == N:
        res = max(res, result)
        return
    
    if tmp + result <= res:
        return

    for i in range(N):
        if board[n][i] != 0 and visited[i] == 0:
            visited[i] = 1
            DFS(n+1, result+board[n][i], tmp - max_val[i])
            visited[i] = 0


T = int(input())
N = 11

for _ in range(T):
    board = [list(map(int, input().split())) for _ in range(N)]
    max_val = []
    for j in range(N):
        tmp = 0
        for i in range(N):
            tmp = max(tmp, board[i][j])
        max_val.append(tmp)
    res = 0
    visited = [0] * N
    DFS(0, 0, sum(max_val))
    print(res)