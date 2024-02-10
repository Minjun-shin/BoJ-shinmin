import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def DFS(num):
    for idx in range(N):
        if ch[idx] == 0 and board[num][idx] == 1:
            ch[idx] = 1
            DFS(idx)


N, M = map(int, input().split())
board = [[0] * N for  _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    board[s-1][e-1] = 1
    board[e-1][s-1] = 1

res = 0
ch = [0] * N
for i in range(N):
    if ch[i] == 0:
        ch[i] = 1
        res += 1
        DFS(i)

print(res)