S1, S2 = input().strip(), input().strip()
LCS = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])