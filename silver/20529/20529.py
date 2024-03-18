from itertools import combinations as comb


T = int(input())

for _ in range(T):
    N = int(input())
    S_list = list(input().split())
    if N >= 33:
        print(0)
        continue

    res = float('inf')
    for s1, s2, s3 in comb(S_list, 3):
        tmp = 0
        for j in range(4):
            if s1[j] != s2[j]:
                tmp += 1
        for j in range(4):
            if s2[j] != s3[j]:
                tmp += 1
        for j in range(4):
            if s3[j] != s1[j]:
                tmp += 1

        res = min(res, tmp)

    print(res)