C, R = map(int, input().split())
K = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

if K > C * R:
    print(0)

else:
    curr = [1, 1]
    while K > 1:
        if direction % 2 == 0:
            dist = R-1
        elif direction == 1:
            dist = C-1
        else:
            dist = C-2

        for _ in range(dist):
            K -= 1
            curr[0] += dx[direction]
            curr[1] += dy[direction]
            if K == 1:
                break

        else:
            if direction == 3:
                K -= 1
                curr[1] += 1
                direction = 0
                R -= 2
                C -= 2

            else:
                direction += 1

    print(*curr)