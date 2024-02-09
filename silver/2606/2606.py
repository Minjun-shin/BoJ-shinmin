def calc(num):
    global res
    for i in range(N):
        if ch[i] == 0 and board[num][i] == 1:
            ch[i] = 1
            res += 1
            calc(i)


N, M = int(input()), int(input())
board = [[0] * N for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    board[s-1][e-1] = 1
    board[e-1][s-1] = 1

ch = [0] * N
ch[0] = 1
res = 0
calc(0)
print(res)