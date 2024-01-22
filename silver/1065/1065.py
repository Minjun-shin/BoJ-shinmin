N = int(input())
res = 0
if N == 1000:
    N -= 1

for num in range(1, N+1):
    num = str(num)
    if len(num) <= 2:
        res += 1
    
    else:
        if int(num[2]) - int(num[1]) == int(num[1]) - int(num[0]):
            res += 1

print(res)