def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def DFS(n=0, result=set()):
    global res
    if n == limit:
        res = max(res, len(result))
        return

    x, y = loca[n]
    for direction in directions[board[x][y]-1]:
        tmp = set()
        for ds in direction:
            for k in range(1, max(N, M)):
                n_x, n_y = x + dr[ds] * k, y + dc[ds] * k

                if is_inrange(n_x, n_y) and board[n_x][n_y] != 6:
                    if board[n_x][n_y] == 0:
                        tmp.add((n_x, n_y))
                else:
                    break

        DFS(n+1, result | tmp)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
directions = [
        ((0,), (1,), (2,), (3,)),
        ((0, 2), (1, 3)),
        ((0, 1), (1, 2), (2, 3), (0, 3)),
        ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)),
        ((0, 1, 2, 3),)
    ]

loca = []
cnt = 0
for r in range(N):
    for c in range(M):
        if board[r][c] in {1, 2, 3, 4, 5}:
            loca.append((r, c))
        if board[r][c] == 0:
            cnt += 1

res = 0
limit = len(loca)
DFS()
print(cnt-res)