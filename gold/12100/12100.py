def DFS(n, arr, idx):
    global res
    if n == 5:
        res = max(res, max(map(max, arr)))
        return

    tmp_arr = [[0] * N for _ in range(N)]
    if idx == 0:
        for c in range(N):
            tmp_que = []
            for r in range(N):
                if arr[r][c]:
                    if (not tmp_que) or tmp_que[-1] != arr[r][c]:
                        tmp_que.append(arr[r][c])
                    elif tmp_que[-1] == arr[r][c]:
                        tmp_que[-1] = str(tmp_que[-1] * 2)
            
            for num_i, num in enumerate(tmp_que):
                tmp_arr[num_i][c] = int(num)

    elif idx == 1:
        for r in range(N):
            tmp_que = []
            for c in range(N-1, -1, -1):
                if arr[r][c]:
                    if (not tmp_que) or tmp_que[-1] != arr[r][c]:
                        tmp_que.append(arr[r][c])
                    elif tmp_que[-1] == arr[r][c]:
                        tmp_que[-1] = str(tmp_que[-1] * 2)
            
            for num_i, num in enumerate(tmp_que):
                tmp_arr[r][N-1-num_i] = int(num)

    elif idx == 2:
        for c in range(N):
            tmp_que = []
            for r in range(N-1, -1, -1):
                if arr[r][c]:
                    if (not tmp_que) or tmp_que[-1] != arr[r][c]:
                        tmp_que.append(arr[r][c])
                    elif tmp_que[-1] == arr[r][c]:
                        tmp_que[-1] = str(tmp_que[-1] * 2)
            
            for num_i, num in enumerate(tmp_que):
                tmp_arr[N-1-num_i][c] = int(num)

    else:
        for r in range(N):
            tmp_que = []
            for c in range(N):
                if arr[r][c]:
                    if (not tmp_que) or tmp_que[-1] != arr[r][c]:
                        tmp_que.append(arr[r][c])
                    elif tmp_que[-1] == arr[r][c]:
                        tmp_que[-1] = str(tmp_que[-1] * 2)
            
            for num_i, num in enumerate(tmp_que):
                tmp_arr[r][num_i] = int(num)

    for i in range(4):
        DFS(n+1, tmp_arr, i)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

res = 0
for idx in range(4):
    DFS(0, board, idx)

print(res)