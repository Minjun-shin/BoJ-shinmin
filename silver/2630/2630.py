def bin_search(r_s, r_e, c_s, c_e):
    global white, blue
    size = (r_e-r_s) * (c_e-c_s)
    total = 0
    for i in range(r_s, r_e):
        for j in range(c_s, c_e):
            total += board[i][j]

    if total == 0:
        white += 1
        return

    if total == size:
        blue += 1
        return

    r_m, c_m = (r_s+r_e)//2, (c_s+c_e)//2
    bin_search(r_s, r_m, c_s, c_m)
    bin_search(r_s, r_m, c_m, c_e)
    bin_search(r_m, r_e, c_s, c_m)
    bin_search(r_m, r_e, c_m, c_e)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0
bin_search(0, N, 0, N)
print(white, blue, sep='\n')