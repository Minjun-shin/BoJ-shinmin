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


N, M = map(int, input().split())
graphs = [[] for _ in range(N)]

edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x : x[2])
    
parents = [i for i in range(N)]
tmp_list = []
cnt = 0

for s, e, w in edges:
    if cnt == N-1:
        break

    if find_set(s-1) == find_set(e-1):
        continue

    tmp_list.append(w)
    union(s-1, e-1)
    cnt += 1
            
tmp_list.sort()

res = 1
for i in range(len(tmp_list)):
    if tmp_list[i] == i + 1:
        res += 1
    else:
        break
    
print(res)