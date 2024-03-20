from collections import deque


def calc(num, cmd):
    if cmd == 'D':
        return (num * 2) % 10000

    elif cmd == 'S':
        return (num - 1) % 10000

    elif cmd == 'L':
        return (num * 10) % 10000 + num // 1000

    else:
        return (num // 10) + (num % 10) * 1000


T = int(input())
for _ in range(T):
    S, E = map(int, input().split())
    check = set()
    check.add(S)
    dQ = deque()
    dQ.append((S, ''))

    while E not in check:
        curr_n, cmds = dQ.popleft()

        for cmd in ['D', 'S', 'L', 'R']:
            new_n = calc(curr_n, cmd)
            if new_n == E:
                print(cmds+cmd)
                break
            if new_n not in check:
                check.add(new_n)
                dQ.append((new_n, cmds+cmd))

        if new_n == E:
            break