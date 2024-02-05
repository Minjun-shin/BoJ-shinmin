from collections import deque


T = int(input())

for _ in range(T):
    N, target = map(int, input().split())
    num_list = deque(map(int, input().split()))
    priority_list = sorted(num_list)

    res = 1
    while True:
        if num_list[0] >= priority_list[-1]:
            num_list.popleft()
            priority_list.pop()

            if target == 0:
                print(res)
                break

            else:
                res += 1
                N -= 1

        else:
            num_list.rotate(-1)
        
        target = (target - 1) % N