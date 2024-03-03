from collections import deque
 
 
def rotate(n, r):
    visited[n] = 1
    if n - 1 >= 0 and visited[n-1] == 0 and magnets[n][6] != magnets[n-1][2]:
        rotate(n-1, -r)
    if n + 1 < 4 and visited[n+1] == 0 and magnets[n][2] != magnets[n+1][6]:
        rotate(n+1, -r)
    magnets[n].rotate(r)
 
 
magnets = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
    
for _ in range(K):
    visited = [0, 0, 0, 0]
    num, rotation = map(int, input().split())
    rotate(num-1, rotation)
 
res = 0
for i in range(4):
    res += magnets[i][0]<<i
 
print(res)