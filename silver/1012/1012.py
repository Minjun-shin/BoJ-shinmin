from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    dQ = deque()

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1

    res = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                board[r][c] = 0
                dQ.append((r, c))
                res += 1
            
            while dQ:
                i, j = dQ.popleft()

                for d in range(4):
                    n_i, n_j = i + dx[d], j + dy[d]

                    if is_inrange(n_i, n_j) and board[n_i][n_j] == 1:
                        board[n_i][n_j] = 0
                        dQ.append((n_i, n_j))

    print(res)