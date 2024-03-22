import sys
input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x, y = find_set(x), find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal():
    res = 0
    cnt = 0

    for s, e, w in edges:
        if cnt == V-1:
            break

        if find_set(s-1) == find_set(e-1):
            continue

        res += w
        union(s-1, e-1)
        cnt += 1

    return res


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x : x[2])
board = [[] for _ in range(V)]

for s, e, w in edges:
    board[s-1].append((e-1, w))
    board[e-1].append((s-1, w))

parents = [i for i in range(V)]
print(kruskal())