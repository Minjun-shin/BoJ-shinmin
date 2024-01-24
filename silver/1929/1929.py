M, N = map(int, input().split())

ch = [0] * (N+1)
ch[0], ch[1] = 1, 1

for num in range(1, N+1):
    if ch[num] == 0:
        for i in range(2*num, N+1, num):
            ch[i] = 1

for x in range(M, N+1):
    if ch[x] == 0:
        print(x)