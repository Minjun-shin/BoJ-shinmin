from collections import deque


N, K = map(int, input().split())

num_list = deque(range(1, N+1))
print('<', end='')

while N > 1:
    num_list.rotate(-K)
    print(f"{num_list.pop()}, ", end='')
    N -= 1

print(f'{num_list.pop()}>')