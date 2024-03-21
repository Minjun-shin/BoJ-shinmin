N = int(input())
M = int(input())
board = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    board[s-1][e-1] = min(board[s-1][e-1], w)

for i in range(N):
    board[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(N):
    for j in range(N):
        if board[i][j] == float('inf'):
            board[i][j] = 0

for row in board:
    print(*row)