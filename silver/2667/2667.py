from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = []

for r in range(N):
    for c in range(N):
        if board[r][c]:
            board[r][c] = 0
            res.append(1)
            dQ = deque()
            dQ.append((r, c))

            while dQ:
                x, y = dQ.popleft()

                for i in range(4):
                    n_x, n_y = x + dx[i], y + dy[i]

                    if is_inrange(n_x, n_y) and board[n_x][n_y]:
                        dQ.append((n_x, n_y))
                        res[-1] += 1
                        board[n_x][n_y] = 0

print(len(res))
for num in sorted(res):
    print(num)