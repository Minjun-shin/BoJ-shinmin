N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                board[i][j] = board[i][k] * board[k][j]

for row in board:
    print(*row)