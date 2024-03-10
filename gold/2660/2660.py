N = int(input())
board = [[float('inf')] * N for _ in range(N)]

while True:
    s, e = map(int, input().split())
    if s == e == -1:
        break

    board[s-1][e-1] = 1
    board[e-1][s-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(N):
    board[i][i] = 0

res_list = [max(board[idx]) for idx in range(N)]
res = [float('inf'), []]
for idx in range(N):
    if res_list[idx] < res[0]:
        res = [res_list[idx], [idx+1]]
    elif res_list[idx] == res[0]:
        res[1].append(idx+1)

print(res[0], len(res[1]))
print(*res[1])