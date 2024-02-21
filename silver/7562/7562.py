from collections import deque


def is_inrange(x, y):
    return 0 <= x < I and 0 <= y < I


def BFS():
    while dQ:
        x, y = dQ.popleft()
        if (x, y) == G:
            print(visited[x][y]-1)
            return
        
        for i in range(8):
            n_x, n_y = x + dx[i], y + dy[i]

            if is_inrange(n_x, n_y) and visited[n_x][n_y] == 0:
                visited[n_x][n_y] = visited[x][y] + 1
                dQ.append((n_x, n_y))


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for _ in range(T):
    I = int(input())
    visited = [[0] * I for _ in range(I)]
    dQ = deque()
    S = tuple(map(int, input().split()))
    visited[S[0]][S[1]] = 1
    dQ.append(S)
    G = tuple(map(int, input().split()))

    BFS()