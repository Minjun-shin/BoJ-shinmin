from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = [[-1] * M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dQ = deque()

for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            res[r][c] = 0
            dQ.append((r, c))

        if board[r][c] == 0:
            res[r][c] = 0

while dQ:
    r, c = dQ.popleft()
    for i in range(4):
        n_r, n_c = r + dr[i], c + dc[i]
        if is_inrange(n_r, n_c) and board[n_r][n_c] == 1:
            board[n_r][n_c] = 0
            dQ.append((n_r, n_c))
            res[n_r][n_c] = res[r][c] + 1

for row in res:
    print(*row)