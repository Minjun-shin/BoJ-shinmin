import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))


def maketree(node, parent):
    for i in connects[node]:
        if i != parent:
            graphs[node].append(i)
            maketree(i, node)


def countnode(node):
    res = 1
    for n_node in graphs[node]:
        countnode(n_node)
        res += counts[n_node]
    counts[node] = res


N, R, Q = map(int, input().split())
connects = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    connects[u].append(v)
    connects[v].append(u)

graphs = [[] for _ in range(N+1)]
maketree(R, -1)

counts = [0] * (N+1)
countnode(R)

for _ in range(Q):
    print(counts[int(input())])