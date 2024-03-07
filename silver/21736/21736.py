from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
dQ = deque()

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(N):
    if dQ:
        break
    for j in range(M):
        if board[i][j] == 'I':
            dQ.append((i, j))
            break

res = 0
while dQ:
    r, c = dQ.popleft()

    for idx in range(4):
        n_r, n_c = r + dr[idx], c + dc[idx]

        if is_inrange(n_r, n_c):
            if board[n_r][n_c] == 'O':
                dQ.append((n_r, n_c))
                board[n_r][n_c] = 'I'
            elif board[n_r][n_c] == 'P':
                dQ.append((n_r, n_c))
                board[n_r][n_c] = 'I'
                res += 1

if res:
    print(res)
else:
    print('TT')