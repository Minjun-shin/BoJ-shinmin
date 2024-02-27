N = int(input())
res = [0] * N
if N >= 1: res[1] = 1
if N >= 2: res[2] = 2

for i in range(3, N):
    res[i] = min(res[i-1], res[i-3]) + 1

if res[N-1] % 2 == 0:
    print('CY')

else:
    print('SK')