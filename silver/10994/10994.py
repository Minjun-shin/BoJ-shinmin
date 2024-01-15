def wrapping():
    global res
    for i in range(len(res)):
        res[i] = [' '] + res[i] + [' ']
    res = [[' '] * len(res[0])] + res + [[' '] * len(res[0])]

    for i in range(len(res)):
        res[i] = ['*'] + res[i] + ['*']
    res = [['*'] * len(res[0])] + res + [['*'] * len(res[0])]


N = int(input())
res = [['*']]

for _ in range(N-1):
    wrapping()

for row in res:
    print(''.join(row))