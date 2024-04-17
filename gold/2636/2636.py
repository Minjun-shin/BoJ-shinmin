from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

start = (0, 0)
dQ = deque()
total = sum(map(sum, board))
cnt = 0

while total:
    cnt += 1
    prev = total
    tmp_list = set()
    visited = [[0] * M for _ in range(N)]
    dQ.append(start)
    while dQ:
        r, c = dQ.popleft()

        for idx in range(4):
            n_r, n_c = r + dr[idx], c + dc[idx]

            if is_inrange(n_r, n_c):
                if board[n_r][n_c] == 0 and visited[n_r][n_c] == 0:
                    visited[n_r][n_c] = 1
                    dQ.append((n_r, n_c))
                elif board[n_r][n_c] == 1:
                    tmp_list.add((n_r, n_c))

    total -= len(tmp_list)
    for r, c in tmp_list:
        board[r][c] = 0

print(cnt, prev, sep='\n')