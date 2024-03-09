N, M = map(int, input().split())
board = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    board[s-1][e-1] = 1
    board[e-1][s-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(N):
    board[i][i] = 0

res = [sum(board[i]) for i in range(N)]
ans = (0, float('inf'))
for idx in range(N):
    if res[idx] < ans[1]:
        ans = (idx+1, res[idx])

print(ans[0])