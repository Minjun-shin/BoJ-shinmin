from itertools import combinations as comb
import math


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')
cnt = 0
limit = math.factorial(N) // math.factorial(N//2) // math.factorial(N//2)
for team1 in comb(range(N), N//2):
    if cnt >= limit or res == 0:
        break
    cnt += 1
    tmp1 = 0
    for num1 in team1:
        for num2 in team1:
            tmp1 += board[num1][num2]

    team2 = [i for i in range(N) if i not in team1]
    tmp2 = 0
    for num1 in team2:
        for num2 in team2:
            tmp2 += board[num1][num2]

    res = min(res, abs(tmp1 - tmp2))

print(res)