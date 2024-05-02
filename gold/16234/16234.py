from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


def calc():
    global stats
    visited = [[0] * N for _ in range(N)]
    new_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                dQ = deque()
                dQ.append((i, j))
                tmp_total = board[i][j]
                tmp_num = [(i, j)]
                
                while dQ:
                    r, c = dQ.popleft()
                    
                    for idx in range(4):
                        nr, nc = r + dr[idx], c + dc[idx]
                        
                        if is_inrange(nr, nc) and visited[nr][nc] == 0 and L <= abs(board[r][c] - board[nr][nc]) <= R:
                            stats = True
                            tmp_total += board[nr][nc]
                            tmp_num.append((nr, nc))
                            visited[nr][nc] = 1
                            dQ.append((nr, nc))
                            
                for r, c in tmp_num:
                    new_arr[r][c] = tmp_total // len(tmp_num)
                    
    return new_arr


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

res = -1
stats = True
while stats:
    res += 1
    stats = False
    board = calc()

print(res)