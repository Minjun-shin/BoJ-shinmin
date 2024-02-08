N, M, inventory = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

MIN, MAX = min(map(min, board)), (sum(map(sum, board)) + inventory) // (N * M)

heights = {}
for r in range(N):
    for c in range(M):
        heights[board[r][c]] = heights.get(board[r][c], 0) + 1

res = (float('inf'), 0)
for target_height in range(MIN, MAX+1):
    tmp_i = inventory
    time = 0
    for height in heights.keys():
        if height > target_height:
            tmp_i += (height - target_height) * heights[height]
            time += (height - target_height) * 2 * heights[height]

        else:
            tmp_i -= (target_height - height) * heights[height]
            time += (target_height - height) * heights[height]

    if tmp_i < 0:
        continue

    if res[0] >= time:
        res = (time, target_height)
    
    else:
        break
    
print(*res)