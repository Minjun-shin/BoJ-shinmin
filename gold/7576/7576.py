from collections import deque


def is_inrange(r, c):
    return 0<= r < M and 0<= c < N


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dQ = deque()
cnt0 = 0
res = 0

for r in range(M):
    for c in range(N):
        if board[r][c] == 0:
            cnt0 += 1
        elif board[r][c] == 1:
            dQ.append((r, c))

while dQ:
    n = len(dQ)
    for _ in range(n):
        curr_x, curr_y = dQ.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if is_inrange(next_x, next_y) and board[next_x][next_y] == 0:
                board[next_x][next_y] = 1
                dQ.append((next_x, next_y))
                cnt0 -= 1
    
    res += 1

if cnt0 == 0:
    print(res-1)
else:
    print(-1)