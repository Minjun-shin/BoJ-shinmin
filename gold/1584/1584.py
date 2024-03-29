from heapq import heappop, heappush


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [[0] * 501 for _ in range(501)]

for num in range(2):
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] = num + 1

dists = [[float('inf')] * 501 for _ in range(501)]
dists[0][0] = 0
pQ = []
heappush(pQ, (0, (0, 0)))

while pQ:
    dist, curr = heappop(pQ)

    if dist > dists[curr[0]][curr[1]] or curr == (500, 500):
        continue

    for idx in range(4):
        n_x, n_y = curr[0] + dx[idx], curr[1] + dy[idx]

        if (0 <= n_x <= 500 and 0 <= n_y <= 500) and board[n_x][n_y] != 2 and dists[n_x][n_y] > dist + board[n_x][n_y]:
            dists[n_x][n_y] = dist + board[n_x][n_y]
            heappush(pQ, (dists[n_x][n_y], (n_x, n_y)))

print(dists[500][500] if dists[500][500] != float('inf') else -1)