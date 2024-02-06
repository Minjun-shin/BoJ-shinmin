from collections import deque


N = int(input())

num_list = deque(range(1, N+1))

while num_list:
    res = num_list.popleft()
    num_list.rotate(-1)

print(res)