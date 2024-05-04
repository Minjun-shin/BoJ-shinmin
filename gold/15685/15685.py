N = int(input())
board = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    sx, sy, d, g = map(int, input().split())
    point_list = [(sx, sy), (sx + dx[d], sy + dy[d])]
    
    for idx in range(g):
        x, y = point_list[-1]
        for r, c in point_list[-2::-1]:
            point_list.append((x - (c - y), y + (r - x)))

    for x, y in point_list:
        board[x][y] = 1

res = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] == 1:
            res += 1

print(res)