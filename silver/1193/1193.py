N = int(input())
cnt = 1
while N > cnt:
    N -= cnt
    cnt += 1

if cnt % 2 == 0:
    print(f"{N}/{cnt+1-N}")
else:
    print(f"{cnt+1-N}/{N}")