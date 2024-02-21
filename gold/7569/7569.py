from collections import deque


def is_inrange(z, x, y):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dz = [0, 0, 0, 0, 1, -1]
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]

dQ = deque()

cnt = 0
for k in range(H):
    for r in range(N):
        for c in range(M):
            if board[k][r][c] == 1:
                dQ.append((k, r, c))
            if board[k][r][c] == 0:
                cnt += 1

res = 0
while dQ:
    res += 1
    for _ in range(len(dQ)):
        z, x, y = dQ.popleft()

        for i in range(6):
            n_z, n_x, n_y = z + dz[i], x + dx[i], y + dy[i]

            if is_inrange(n_z, n_x, n_y) and board[n_z][n_x][n_y] == 0:
                board[n_z][n_x][n_y] = 1
                dQ.append((n_z, n_x, n_y))
                cnt -= 1

if cnt:
    print(-1)
else:
    print(res-1)