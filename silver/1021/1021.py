from collections import deque


N, M = map(int, input().split())
num_list = deque(range(1, N+1))
wanted = list(map(int, input().split()))

res = 0
for num in wanted:
    idx = num_list.index(num)
    if idx*2 <= len(num_list):
        num_list.rotate(-idx)
        res += idx
    else:
        num_list.rotate(len(num_list)-idx)
        res += len(num_list)-idx

    num_list.popleft()

print(res)