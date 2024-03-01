N = int(input())

cols = [0] * 1001  # 높이들을 위치에 맞춰 저장
max_loc = 0  # 기둥들 중 오른쪽 끝의 위치
min_loc = float('inf')  # 기둥들 중 왼쪽 끝의 위치
highest = (0, 0)  # 가장 높은 기둥의 위치와 높이

for _ in range(N):
    l, h = map(int, input().split())
    cols[l] = h
    highest = max(highest, (l, h), key=lambda x : x[1])
    max_loc = max(max_loc, l)
    min_loc = min(min_loc, l)

res = highest[1]
height = 0  # 현재 순회 중인 위치까지의 최대 높이
for i in range(min_loc, highest[0]):
    height = max(height, cols[i])
    res += height

height = 0
for i in range(max_loc, highest[0], -1):
    height = max(height, cols[i])
    res += height

print(res)