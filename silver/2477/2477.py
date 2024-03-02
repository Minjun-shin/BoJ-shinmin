from collections import deque


K = int(input())
directions = deque()
lengths = deque()
for _ in range(6):
    d, l = map(int, input().split())
    directions.append(d)
    lengths.append(l)

while not (directions.count(directions[0]) == 1 and directions.count(directions[1]) == 1):
    directions.rotate(1)
    lengths.rotate(1)

print(K * ((lengths[0] * lengths[1]) - (lengths[3] * lengths[4])))