board = [list(map(int, input().split())) for _ in range(5)]
ch = [0] * 12
hashmap = {board[r][c] : (r, c) for r in range(5) for c in range(5)}

res = 0
tmp = False
for _ in range(5):
    if tmp:
        break
    num_list = list(map(int, input().split()))
    for num in num_list:
        res += 1
        ch[hashmap[num][0]] += 1
        ch[hashmap[num][1] + 5] += 1
        if hashmap[num][0] ==hashmap[num][1]:
            ch[-2] += 1

        if sum(hashmap[num]) == 4:
            ch[-1] += 1

        if ch.count(5) >= 3:
            print(res)
            tmp = True
            break