from heapq import heappop, heappush


def is_inrange(x, y):
    return 0 <= x < M and 0 <= y < N


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(M)]

pQ = [(0, 0, 0)]
nums = [[float('inf')] * N for _ in range(M)]
nums[0][0] = 0

while pQ:
    num, r, c = heappop(pQ)

    if (r, c) == (M-1, N-1) or num > nums[r][c]:
        continue

    for idx in range(4):
        nr, nc = r + dr[idx], c + dc[idx]

        if is_inrange(nr, nc) and nums[nr][nc] > num + board[nr][nc]:
            nums[nr][nc] = num + board[nr][nc]
            heappush(pQ, (nums[nr][nc], nr, nc))

print(nums[-1][-1])