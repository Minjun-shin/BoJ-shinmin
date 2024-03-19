from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


N = int(input())
board = [list(input().strip()) for _ in range(N)]
dQ = deque()
res = [0, 0]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            dQ.append((r, c))
            visited[r][c] = 1
            res[0] += 1
            color = board[r][c]

            while dQ:
                x, y = dQ.popleft()

                for i in range(4):
                    n_x, n_y = x + dx[i], y + dy[i]

                    if is_inrange(n_x, n_y) and visited[n_x][n_y] == 0 and board[n_x][n_y] == color:
                        dQ.append((n_x, n_y))
                        visited[n_x][n_y] = 1

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            dQ.append((r, c))
            visited[r][c] = 1
            res[1] += 1
            if board[r][c] == 'B':
                color = {board[r][c]}
            else:
                color = {'R', 'G'}

            while dQ:
                x, y = dQ.popleft()

                for i in range(4):
                    n_x, n_y = x + dx[i], y + dy[i]

                    if is_inrange(n_x, n_y) and visited[n_x][n_y] == 0 and board[n_x][n_y] in color:
                        dQ.append((n_x, n_y))
                        visited[n_x][n_y] = 1

print(*res)