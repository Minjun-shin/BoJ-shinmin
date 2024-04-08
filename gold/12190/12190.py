from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


def calc(x, y):
    res = False
    for idx in range(8):
        n_x, n_y = x + dr[idx], y + dc[idx]
        if is_inrange(n_x, n_y):
            res = res or (board[n_x][n_y] == '*')
    return res


dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    ch = [[0] * N for _ in range(N)]
    result = 0
    
    for i in range(N):
        for j in range(N):
            if ch[i][j] == 0 and board[i][j] == '.' and not calc(i, j):
                result += 1
                ch[i][j] = 1
                dQ = deque()
                dQ.append((i, j))

                while dQ:
                    r, c = dQ.popleft()

                    for idx in range(8):
                        n_r, n_c = r + dr[idx], c + dc[idx]

                        if is_inrange(n_r, n_c) and ch[n_r][n_c] == 0 and board[n_r][n_c] == '.':
                            ch[n_r][n_c] = 1
                            if not calc(n_r, n_c):
                                dQ.append((n_r, n_c))
    for i in range(N):
        for j in range(N):
            if ch[i][j] == 0 and board[i][j] == '.':
                result += 1

    print(f"Case #{test_case}: {result}")