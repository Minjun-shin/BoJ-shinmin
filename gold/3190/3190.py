from collections import deque


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
snake = deque([(0, 0)])
time = 0
D = 0

N, K = int(input()), int(input())
apples = set()

for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

L = int(input())

end = False

for _ in range(L):
    num, C = input().split()
    if end:
        break
    num = int(num)

    while time < num:
        time += 1
        n_x, n_y = snake[-1][0] + dx[D], snake[-1][1] + dy[D]
        if is_inrange(n_x, n_y) and (n_x, n_y) not in snake:
            snake.append((n_x, n_y))
            if (n_x, n_y) not in apples:
                t_x, t_y = snake.popleft()
            else:
                apples.discard((n_x, n_y))
        else:
            end = True
            break
    
    if not end:
        if C == 'D':
            D = (D + 1) % 4
        else:
            D = (D - 1) % 4

if not end:
    while True:
        time += 1
        n_x, n_y = snake[-1][0] + dx[D], snake[-1][1] + dy[D]
        if is_inrange(n_x, n_y) and (n_x, n_y) not in snake:
            snake.append((n_x, n_y))
            if (n_x, n_y) not in apples:
                t_x, t_y = snake.popleft()
            else:
                apples.discard((n_x, n_y))
        else:
            break

print(time)