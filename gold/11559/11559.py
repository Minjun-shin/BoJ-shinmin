from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def popping():
    visited = [[0] * M for _ in range(N)]
    ans = False

    for i in range(N):
        for j in range(M):
            if board[i][j] != '.' and visited[i][j] == 0:
                tmp = set()
                dQ = deque()
                tmp.add((i, j))
                dQ.append((i, j))

                while dQ:
                    r, c = dQ.popleft()

                    for idx in range(4):
                        nr, nc = r + dr[idx], c + dc[idx]

                        if is_inrange(nr, nc) and visited[nr][nc] == 0 and board[nr][nc] == board[r][c]:
                            visited[nr][nc] = 1
                            tmp.add((nr, nc))
                            dQ.append((nr, nc))

                if len(tmp) >= 4:
                    ans = True
                    for r, c in tmp:
                        board[r][c] = '.'

    return ans


def droping():
    stats = True

    while stats:
        stats = False
        for i in range(N-2, -1, -1):
            for j in range(M):
                if board[i][j] != '.' and board[i+1][j] == '.':
                    stats = True
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j]


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = 12, 6
board = [list(input().strip()) for _ in range(N)]
res = 0

while popping():
    res += 1
    droping()

print(res)