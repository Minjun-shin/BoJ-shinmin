def d(n):
    return n + sum(map(int, str(n)))

N = 9999
res = [0] * N

for num in range(N):
    if res[num] == 0:
        print(num+1)
    
    if d(num+1) <= N:
        res[d(num+1)-1] = 1