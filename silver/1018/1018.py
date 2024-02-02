N, M = map(int, input().split())
board = [list(map(lambda x : 1 if x == 'W' else 0, input())) for _ in range(N)]

res = 64
for r in range(N-7):
    for c in range(M-7):
        tmp = 0
        for i in range(8):
            for j in range(8):
                if board[r+i][c+j] != ((i + j) % 2):
                    tmp += 1
        
        res = min([res, tmp, 64 - tmp])

print(res)