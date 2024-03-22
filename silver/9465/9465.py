T = int(input())

for _ in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    res = [[0, 0, 0] for _ in range(N+1)]

    for i in range(1, N+1):
        res[i][0] = max(res[i-1][1], res[i-1][2]) + board[0][i-1]
        res[i][1] = max(res[i-1][0], res[i-1][2]) + board[1][i-1]
        res[i][2] = max(res[i-1])

    print(max(res[-1]))