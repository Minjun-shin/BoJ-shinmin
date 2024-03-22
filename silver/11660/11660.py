import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    board[0][i] = board[0][i] + board[0][i-1]
    board[i][0] = board[i][0] + board[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        board[i][j] = board[i][j] + board[i-1][j] + board[i][j-1] - board[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = board[x2-1][y2-1]
    res -= board[x2-1][y1-2] if y1 > 1 else 0
    res -= board[x1-2][y2-1] if x1 > 1 else 0
    res += board[x1-2][y1-2] if x1 > 1 and y1 > 1 else 0
    print(res)