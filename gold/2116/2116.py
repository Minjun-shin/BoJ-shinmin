N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

res = 0
for num in range(1, 7):
    n = 0
    total = 0
    while n < N:
        idx = dices[n].index(num)
        if idx == 0:
            num = dices[n][5]
            total += max(dices[n][1], dices[n][2], dices[n][3], dices[n][4])

        elif idx == 1:
            num = dices[n][3]
            total += max(dices[n][0], dices[n][2], dices[n][4], dices[n][5])

        elif idx == 2:
            num = dices[n][4]
            total += max(dices[n][0], dices[n][1], dices[n][3], dices[n][5])

        elif idx == 3:
            num = dices[n][1]
            total += max(dices[n][0], dices[n][2], dices[n][4], dices[n][5])

        elif idx == 4:
            num = dices[n][2]
            total += max(dices[n][0], dices[n][1], dices[n][3], dices[n][5])

        else:
            num = dices[n][0]
            total += max(dices[n][1], dices[n][2], dices[n][3], dices[n][4])

        n += 1
    
    res = max(res, total)

print(res)