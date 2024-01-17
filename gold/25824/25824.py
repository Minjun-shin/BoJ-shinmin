from math import inf

def DFS(n, prev, result):
    global res
    if n == 5:
        res = min(res, result)
        return
    
    for i in range(2):
        DFS(n+1, groups[n+1][i], result+board[sum(groups[n])-prev][groups[n+1][i]])


board = [list(map(int, input().split())) for _ in range(12)]
res = inf
common= sum([board[2 * i][2 * i + 1] for i in range(6)])
groups = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]

for i in range(2):
    DFS(0, i, 0)

print(res + common)