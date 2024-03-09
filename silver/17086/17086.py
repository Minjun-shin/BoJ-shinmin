from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dQ = deque()

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            dQ.append((r, c))

while dQ:
    r, c = dQ.popleft()

    for i in range(8):
        n_r, n_c = r + dr[i], c + dc[i]

        if is_inrange(n_r, n_c) and board[n_r][n_c] == 0:
            board[n_r][n_c] = board[r][c] + 1
            dQ.append((n_r, n_c))

print(max(map(max, board)) - 1)