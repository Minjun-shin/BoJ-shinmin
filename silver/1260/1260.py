from collections import deque


def DFS(num):
    print(num+1, end=' ')
    for i in range(N):
        if board[num][i] == 1 and visited_DFS[i] == 0:
            visited_DFS[i] = 1
            DFS(i)


def BFS(num):
    dQ = deque()
    dQ.append(num)
    res = [num+1]
    visited_BFS = [0] * N
    visited_BFS[num] = 1

    while dQ:
        curr = dQ.popleft()

        for i in range(N):
            if board[curr][i] == 1 and visited_BFS[i] == 0:
                visited_BFS[i] = 1
                res.append(i+1)
                dQ.append(i)

    print(*res)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    for _ in range(M):
        s, e = map(int, input().split())
        board[s-1][e-1] = 1
        board[e-1][s-1] = 1

    visited_DFS = [0] * N
    visited_DFS[V-1] = 1
    DFS(V-1)
    print()
    BFS(V-1)