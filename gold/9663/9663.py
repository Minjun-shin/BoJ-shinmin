def DFS(n):
    global res
    if n == N:
        res += 1
        return
    
    for i in range(N):
        if ch[i] == 0 and ch_D1[n+i] == 0 and ch_D2[n-i+N-1] == 0:
            ch[i] = 1
            ch_D1[n+i] = 1
            ch_D2[n-i+N-1] = 1
            DFS(n+1)
            ch[i] = 0
            ch_D1[n+i] = 0
            ch_D2[n-i+N-1] = 0


N = int(input())
ch = [0] * N
ch_D1 = [0] * (2*N-1)
ch_D2 = [0] * (2*N-1)
res = 0
DFS(0)
print(res)