def calc(N, M):
    cnt = 1
    while M != N:
        cnt += 1
        if M % 2 == 0:
            M //= 2
        elif M % 10 == 1:
            M //= 10
        else:
            return -1
        if M < N:
            return -1
    return cnt

N, M = map(int, input().split())
print(calc(N, M))