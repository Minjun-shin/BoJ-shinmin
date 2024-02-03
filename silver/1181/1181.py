N = int(input())

res = []
for _ in range(N):
    s = input()
    if s not in res:
        res.append(s)

print(*sorted(res, key=lambda x : (len(x), x)), sep='\n')