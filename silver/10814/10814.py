import sys
input = sys.stdin.readline


N = int(input())
res = []

for i in range(N):
    age, name = input().split()
    res.append((int(age), i, name))

res.sort()

for age, _, name in res:
    print(age, name)