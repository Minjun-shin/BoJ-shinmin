T = int(input())

for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue

    if N == 1:
        print(0, 1)
        continue
    
    res0 = [0] * (N+1)
    res1 = [0] * (N+1)
    res0[0], res1[1] = 1, 1

    for i in range(2, N+1):
        res0[i] = res0[i-1] + res0[i-2]
        res1[i] = res1[i-1] + res1[i-2]

    print(res0[-1], res1[-1])