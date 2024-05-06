def calc(arr, B):
    if B == 1:
        return arr
    
    tmp = calc(arr, B//2)
    
    ans = [[0] * N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ans[i][j] = (ans[i][j] + tmp[i][k] * tmp[k][j]) % 1000

    if B % 2 == 0:
        return ans
    
    else:
        ans2 = [[0] * N for _ in range(N)]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    ans2[i][j] = (ans2[i][j] + ans[i][k] * arr[k][j]) % 1000
        return ans2


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = calc(arr, B)
for row in answer:
    for each in row:
        print(each % 1000, end=' ')
    print()