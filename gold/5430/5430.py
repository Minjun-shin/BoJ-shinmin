from collections import deque


T = int(input())
for _ in range(T):
    cmd = input().strip()
    N = int(input())
    num_list = deque()
    for letter in input().lstrip('[').rstrip(']').split(','):
        if letter:
            num_list.append(int(letter))
    state = 0

    for letter in cmd:
        if letter == 'R':
            state = (state + 1) % 2

        else:
            if not num_list:
                state = -1
                break
            if state == 0:
                num_list.popleft()

            else:
                num_list.pop()

    if state == -1:
        print('error')
    elif state == 1:
        print('[', end='')
        print(*list(num_list)[::-1], sep=',', end=']\n')
    else:
        print('[', end='')
        print(*list(num_list), sep=',', end=']\n')