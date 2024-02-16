def DFS(n, result=[], idx=-1):
    if n == 6:
        print(*result)
        return
    
    for i in range(idx+1, k):
        DFS(n + 1, result + [S[i]], i)


while True:
    k, *S = map(int, input().split())
    if k == 0:
        break

    DFS(0)
    print()