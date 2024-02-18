def DFS(n, result):
    if n == M:
        if result not in res:
            print(*result)
            res.add(result)
        return
    
    for i in range(N):
        if ch[i] == 0:
            ch[i] = 1
            DFS(n+1, result+(num_list[i],))
            ch[i] = 0
    

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ch = [0] * N

res = set()
DFS(0, ())