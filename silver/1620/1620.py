import sys
input = sys.stdin.readline


N, M = map(int, input().split())

to_num, to_str = {}, {}
for i in range(1, N+1):
    name = input().strip()
    to_num[name.lower()] = i
    to_str[i] = name

for _ in range(M):
    s = input().strip()
    if s.isdecimal():
        print(to_str[int(s)])

    else:
        print(to_num[s.lower()])