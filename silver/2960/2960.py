N, M = map(int, input().split())
ch = [0] * (N+1)

for i in range(2, N+1):
    if M == 0:
        break
    if ch[i] == 0:
        for j in range(i, N+1, i):
            if ch[j] == 0:
                M -= 1
                if M == 0:
                    res = j
                    break
                ch[j] = 1
            

print(res)