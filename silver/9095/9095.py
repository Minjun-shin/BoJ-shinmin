T = int(input())

for _ in range(T):
    N = int(input())
    ch = [0] * max((N + 1), 4)
    ch[1], ch[2], ch[3] = 1, 2, 4

    for i in range(4, N+1):
        ch[i] = ch[i-1] + ch[i-2] + ch[i-3]

    print(ch[N])