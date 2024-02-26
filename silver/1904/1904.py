N = int(input())
ch = [0] * (N+1)
ch[0], ch[1] = 1, 1

for i in range(2, N+1):
    ch[i] = (ch[i-1] + ch[i-2]) % 15746

print(ch[-1])