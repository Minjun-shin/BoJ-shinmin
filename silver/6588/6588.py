import sys
input = sys.stdin.readline


ch = [0] * (1000000+1)
ch[0], ch[1] = 1, 1

for num in range(2, 1000000+1):
    if ch[num] == 0:
        for i in range(2*num, 1000000+1, num):
            ch[i] = 1

while True:
    N = int(input())
    if N == 0:
        break

    for idx in range(3, N // 2 + 1, 2):
        if ch[idx] == 0 and ch[N-idx] == 0:
            print(f"{N} = {idx} + {N-idx}")
            break

    else:
        print("Goldbach's conjecture is wrong.")