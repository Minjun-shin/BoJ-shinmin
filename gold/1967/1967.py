def DFS(num):
    global res, node
    stack = [(num, 0)]
    visited = [0] * N
    visited[num] = 1

    while stack:
        curr, dist = stack.pop()
        if dist > res:
            res = dist
            node = curr

        for new_n, weight in graphs[curr]:
            if visited[new_n] == 0:
                visited[new_n] = 1
                stack.append((curr, dist))
                stack.append((new_n, dist + weight))
                break
        


N = int(input())
graphs = [[] for _ in range(N)]

for _ in range(N-1):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))
    graphs[e-1].append((s-1, w))

res = 0
node = 0
DFS(0)
DFS(node)
print(res)