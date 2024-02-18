def DFS(n, result):
    if n == M:
        print(*result)
        return
    
    for i in range(len(num_list)):
        DFS(n+1, result+(num_list[i],))
    

N, M = map(int, input().split())
num_list = set(map(int, input().split()))
num_list = sorted(num_list)

DFS(0, ())