S = input().strip()
N = len(S)
res = []
for first in range(N-2):
    for second in range(first+1, N-1):
        res.append(S[:first+1][::-1]+S[first+1:second+1][::-1]+S[second+1:][::-1])

res.sort()
print(res[0])