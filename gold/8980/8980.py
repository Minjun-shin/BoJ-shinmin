N, C = map(int, input().split())
M = int(input())
boxes = [{} for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    boxes[s-1][e-1] = w
    
res = 0
truck = {i:0 for i in range(1, N+1)}
truck['curr'] = 0

for s in range(N):
    res += truck.get(s, 0)
    truck['curr'] -= truck.get(s, 0)
    truck[s] = 0
    for e, w in boxes[s].items():
        truck['curr'] += w
        truck[e] += w
    pointer = N
    while truck['curr'] > C:
        load = min(truck['curr'] - C, truck[pointer])
        truck['curr'] -= load
        truck[pointer] -= load
        pointer -= 1

print(res)