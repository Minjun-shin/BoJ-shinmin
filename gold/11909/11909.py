N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dists = [[0] * N for _ in range(N)]

for i in range(1, N):
    dists[0][i] = dists[0][i-1] + max(0, board[0][i] - board[0][i-1] + 1)
    dists[i][0] = dists[i-1][0] + max(0, board[i][0] - board[i-1][0] + 1)

for r in range(1, N):
    for c in range(1, N):
        dists[r][c] = min(dists[r-1][c] + max(0, board[r][c] - board[r-1][c] + 1), dists[r][c-1] + max(0, board[r][c] - board[r][c-1] + 1))
            
print(dists[-1][-1])