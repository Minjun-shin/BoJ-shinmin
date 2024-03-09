from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
size, eating = 2, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            curr = (i, j)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

state = True
cnt = 0
while state:
    dQ = deque()
    dQ.append(curr)
    fishes = set()
    tmp_cnt = 0
    visited = [[0] * N for _ in range(N)]
    visited[curr[0]][curr[1]] = 1
    while dQ and (not fishes):
        tmp_cnt += 1
        for _ in range(len(dQ)):
            x, y = dQ.popleft()

            for i in range(4):
                n_x, n_y = x + dx[i], y + dy[i]

                if is_inrange(n_x, n_y):
                    if (board[n_x][n_y] == size or board[n_x][n_y] == 0) and visited[n_x][n_y] == 0:
                        visited[n_x][n_y] = 1
                        dQ.append((n_x, n_y))
                    elif board[n_x][n_y] < size and visited[n_x][n_y] == 0:
                        visited[n_x][n_y] = 1
                        fishes.add((n_x, n_y))

    if not fishes:
        state = False
    else:
        board[curr[0]][curr[1]] = 0
        curr = sorted(fishes)[0]
        board[curr[0]][curr[1]] = 9
        eating += 1
        if eating >= size:
            size += 1
            eating = 0
        cnt += tmp_cnt

print(cnt)