import sys
input = sys.stdin.readline


dna_list = ['A', 'C', 'G', 'T']
N, M = map(int, input().split())

dnas = [input() for _ in range(N)]
res = ''
res_num = 0

for i in range(M):
    tmp = ''
    num = 0
    tmp_s = ''
    for j in range(N):
        tmp += dnas[j][i]
    
    for letter in dna_list:
        if tmp.count(letter) > num:
            num = tmp.count(letter)
            tmp_s = letter
    
    res += tmp_s
    res_num += N - num

print(res)
print(res_num)