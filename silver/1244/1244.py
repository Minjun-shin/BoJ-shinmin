N = int(input())
switches = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    S, num = map(int, input().split())
    if S == 1:
        for i in range(num, N+1, num):
            switches[i-1] ^= 1

    else:
        i = 0
        for i in range(1, min(num, N-num+1)):
            if switches[num - 1 - i] != switches[num - 1 + i]:
                break

        else:
            switches[num - 1 - i] ^= 1
            switches[num - 1 + i] ^= 1

        for idx in range(num-i, num+i-1):
            switches[idx] ^= 1

        if i == 0: # if num is end of start idx
            switches[num-1] ^= 1

for i in range(N):
    if i > 0 and i % 20 == 0:
        print()
    print(switches[i], end=' ')
