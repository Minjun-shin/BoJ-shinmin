import sys
sys.setrecursionlimit(10**6)


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def DFS(r, c):
    if visited[r][c] >= 0:
        return visited[r][c]
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if is_inrange(nr, nc) and board[r][c] > board[nr][nc]:
            visited[r][c] += DFS(nr, nc)

    visited[r][c] += 1
    return visited[r][c]


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
visited[N-1][M-1] = 1

print(DFS(0, 0))