def is_inrange(x, y):
    return 0 <= x < R and 0 <= y < C


def abroad():
    tmp_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                amount = board[r][c] // 5

                for idx in range(4):
                    nr, nc = r + dr[idx], c + dc[idx]

                    if is_inrange(nr, nc) and (nr, nc) not in cleaner:
                        tmp_board[r][c] -= amount
                        tmp_board[nr][nc] += amount

    for r in range(R):
        for c in range(C):
            board[r][c] += tmp_board[r][c]


def cycle(r, c, lo):
    direct = 0
    prev = 0
    r, c = r + dr[direct], c + dc[direct]

    while board[r][c] >= 0:
        prev, board[r][c] = board[r][c], prev
        nr, nc = r + dr[direct], c + dc[direct]
        if not is_inrange(nr, nc):
            direct = (direct + lo) % 4
            nr, nc = r + dr[direct], c + dc[direct]
        r, c = nr, nc


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        break

cleaner = [(i, 0), (i+1, 0)]

for _ in range(T):
    for row in board:
        print(*row)
    print()
    abroad()
    for row in board:
        print(*row)
    print()
    cycle(*cleaner[0], -1)
    cycle(*cleaner[1], 1)

print(sum(map(sum, board)) + 2)