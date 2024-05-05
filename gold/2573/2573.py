from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < M


def simul():
    new_arr = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] > 0:
                tmp = board[i][j]
                
                for idx in range(4):
                    nr, nc = i + dr[idx], j + dc[idx]
                    
                    if board[nr][nc] == 0:
                        tmp -= 1
                
                new_arr[i][j] = max(0, tmp)
    
    return new_arr


def calc():
    result = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] > 0:
                result += 1
                dQ = deque()
                dQ.append((i, j))
                visited[i][j] = 1
                
                while dQ:
                    r, c = dQ.popleft()
                    
                    for idx in range(4):
                        nr, nc = r + dr[idx], c + dc[idx]
                        
                        if is_inrange(nr, nc) and visited[nr][nc] == 0 and board[nr][nc] > 0:
                            visited[nr][nc] = 1
                            dQ.append((nr, nc))
                            
    return result


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

res = 0
while True:
    res += 1
    board = simul()
    
    cnt = calc()
    if cnt == 0:
        res = 0
        break
    
    elif cnt > 1:
        break
    
print(res)