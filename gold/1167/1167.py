from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def djikstra(start):
    global res, node
    dists = [float('inf')] * V
    dists[start] = 0
    pq = [(0, start)]
    while pq:
        dist, curr = heappop(pq)
        if dist > dists[curr]:
            continue
        
        for i, w in nodes[curr]:
            if dists[i] > dist + w:
                dists[i] = dist + w
                if res < dists[i]:
                    res = dists[i]
                    node = i
                heappush(pq, (dists[i], i))


V = int(input())
nodes = [[] for _ in range(V)]

for _ in range(V):
    num, *num_list = map(int, input().split())
    for i in range(0, len(num_list)-1, 2):
        nodes[num-1].append((num_list[i]-1, num_list[i+1]))

res = 0
node = 0
djikstra(0)
djikstra(node)
print(res)