def wrapping():
    global res
    r, c = len(res[0]), len(res)
    for i in range(c):
        res[i] = ['*', ' '] + res[i] + [' ', '*']
    res = [
        ['*'] * (r + 4),
        ['*'] + [' '] * (r + 2) + ['*']
        ] + res + [
            ['*'] + [' '] * (r + 2) + ['*'],
            ['*'] * (r + 4)
        ]
    res[1][-1], res[2][-2] = ' ', '*'


N = int(input())
res = list(map(list, ['*****', '*    ', '* ***', '* * *', '* * *', '*   *', '*****']))
for _ in range(N-2):
    wrapping()

if N != 1:
    for row in res:
        print(''.join(row).strip())

else:
    print('*')