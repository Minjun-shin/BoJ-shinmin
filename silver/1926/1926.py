from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt, max_a = 0, 0
dQ = deque()

for r in range(N):
    for c in range(M):
        if board[r][c]:
            cnt += 1
            tmp = 0
            board[r][c] = 0
            dQ.append((r, c))

            while dQ:
                tmp += 1
                curr_x, curr_y = dQ.popleft()

                for i in range(4):
                    next_x, next_y = curr_x + dx[i], curr_y + dy[i]

                    if is_inrange(next_x, next_y) and board[next_x][next_y]:
                        board[next_x][next_y] = 0
                        dQ.append((next_x, next_y))
            
            max_a = max(max_a, tmp)

print(cnt, max_a, sep='\n')