from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def calc():
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    dQ = deque([(0, 0)])
    cheezes = set()
    stats = False
    
    while dQ:
        r, c = dQ.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if is_inrange(nr, nc):
                if board[nr][nc] == 1:
                    if visited[nr][nc] == 1:
                        cheezes.add((nr, nc))
                    else:
                        visited[nr][nc] = 1
                elif visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    dQ.append((nr, nc))
    
    if cheezes:
        stats = True
        for r, c in cheezes:
            board[r][c] = 0
            
    return stats


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

res = 0
while calc():
    res += 1
    
print(res)