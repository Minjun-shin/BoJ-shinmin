from heapq import heappop, heappush


def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

test_case = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = board[0][0]

    pQ = [(dists[0][0], 0, 0)]

    while pQ:
        dist, r, c = heappop(pQ)

        if dist > dists[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if is_inrange(nr, nc) and (dists[nr][nc] > dist + board[nr][nc]):
                dists[nr][nc] = dist + board[nr][nc]
                heappush(pQ, (dists[nr][nc], nr, nc))

    print(f"Problem {test_case}: {dists[-1][-1]}")
    test_case += 1