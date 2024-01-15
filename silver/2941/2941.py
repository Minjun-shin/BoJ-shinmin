sp_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
N = len(s)
res = N
for idx in range(N):
    if s[idx] not in ['c', 'd', 'l', 'n', 's', 'z']:
        continue

    if s[idx:idx+2] in sp_list or s[idx:idx+3] == 'dz=':
        res -= 1

print(res)