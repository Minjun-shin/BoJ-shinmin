import sys
input = sys.stdin.readline


N = int(input())

total = set()
for _ in range(N):
    name, cmd = input().split()

    if cmd == 'enter':
        total.add(name)

    else:
        total.discard(name)

for name in sorted(total, reverse=True):
    print(name)