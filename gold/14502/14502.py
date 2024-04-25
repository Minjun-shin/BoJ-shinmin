from itertools import combinations as comb
from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def BFS():
    for R in range(N):
        for C in range(M):
            if board[R][C] == 2 and visited[R][C] == 0:
                visited[R][C] = 1
                dQ = deque()
                dQ.append((R, C))
                while dQ:
                    r, c = dQ.popleft()
                    
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        
                        if is_inrange(nr, nc) and board[nr][nc] == 0 and visited[nr][nc] == 0 and (nr, nc) not in [(i1, j1), (i2, j2), (i3, j3)]:
                            visited[nr][nc] = 1
                            dQ.append((nr, nc))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
loc_list = [(i, j) for i in range(N) for j in range(M)]

res = 0
for (i1, j1), (i2, j2), (i3, j3) in comb(loc_list, 3):
    if board[i1][j1] != 0 or board[i2][j2] != 0 or board[i3][j3] != 0:
        continue
    visited = [[0] * M for _ in range(N)]
    BFS()
    tmp = -3
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0 and visited[r][c] == 0:
                tmp += 1
    res = max(res, tmp)
        
print(res)