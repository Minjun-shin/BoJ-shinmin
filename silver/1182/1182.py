def DFS(n, result):
    global res
    if n == N:
        if result and sum(result) == S:
            res += 1
        return
     
    DFS(n+1, result+[num_list[n]])
    DFS(n+1, result)
 
 
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
res = 0
DFS(0, [])
print(res)