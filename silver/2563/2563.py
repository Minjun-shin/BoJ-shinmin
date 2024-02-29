board = [[0] * 100 for _ in range(100)]

N = int(input())
for _ in range(N):
    left, bottom = map(int,input().split())

    for i in range(10):
        for j in range(10):
            board[left+i][bottom+j] = 1

print(sum(map(sum, board)))