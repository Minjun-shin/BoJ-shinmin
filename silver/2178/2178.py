from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dQ = deque([(0, 0)])
board[0][0] = 0
res = 1

while dQ:
    if (N-1, M-1) in dQ:
        break
    n = len(dQ)
    for _ in range(n):
        curr_x, curr_y = dQ.popleft()

        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]

            if is_inrange(next_x, next_y) and board[next_x][next_y]:
                board[next_x][next_y] = 0
                dQ.append((next_x, next_y))

    res += 1

print(res)