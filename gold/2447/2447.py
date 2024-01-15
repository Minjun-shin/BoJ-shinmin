res = [['***'], ['* *'], ['***']]
N = int(input())

while N != 3:
    l = len(res)
    for i in range(l):
        res[i] *= 3

    for _ in range(2):
        for i in range(l):
            res.append(res[i].copy())

    for i in range(len(res)):
        if i // l == 1:
            res[i][1] = ' ' * l

    for i in range(l*3):
        res[i] = [''.join(res[i])]
    
    N //= 3

for row in res:
    print(*row)