cnt = 0
res = 0
N = int(input())

while cnt < N:
    res += 1
    if '666' in str(res):
        cnt += 1

print(res)