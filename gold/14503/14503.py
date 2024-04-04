def calc(r, c, d):
    visited[r][c] = 1
    res = 1
    while True:
        state = True
        for i in range(4):
            n_r, n_c = r + dx[i], c + dy[i]

            state = state and bool(visited[n_r][n_c])

        if state:
            n_r, n_c = r + dx[(d-2)%4], c + dy[(d-2)%4]

            if board[n_r][n_c] == 1:
                return res
            else:
                r, c = n_r, n_c

        else:
            d = (d - 1) % 4
            n_r, n_c = r + dx[d], c + dy[d]

            if visited[n_r][n_c] == 0:
                res += 1
                r, c = n_r, n_c
                visited[r][c] = 1


N, M = map(int, input().split())
R, C, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [row.copy() for row in board]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(calc(R, C, D))