N = int(input())
res = [0] * max((abs(N)+1), 2)
res[1] = 1

if N >= 0:
    for i in range(2, N+1):
        res[i] = (res[i-1] + res[i-2]) % 1000000000

else:
    N *= -1
    for i in range(2, N+1):
        res[i] = res[i-2] - res[i-1]
        res[i] = (res[i] // abs(res[i])) * (abs(res[i]) % 1000000000)

if N:
    print(res[-1] // abs(res[-1]))
    print(abs(res[-1]))

else:
    print(0)
    print(0)