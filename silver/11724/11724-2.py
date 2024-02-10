from collections import deque
import sys
input = sys.stdin.readline


def BFS(num):
    dQ = deque([num])
    while dQ:
        curr = dQ.popleft()
        for idx in range(N):
            if ch[idx] == 0 and board[curr][idx]:
                ch[idx] = 1
                dQ.append(idx)


N, M = map(int, input().split())
board = [[0] * N for  _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    board[s-1][e-1] = 1
    board[e-1][s-1] = 1

ch = [0] * N
res = 0
for i in range(N):
    if ch[i] == 0:
        res += 1
        BFS(i)

print(res)