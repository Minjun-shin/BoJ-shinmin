import heapq
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    checked = [0] * K

    for idx in range(K):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            checked[idx] = 1

        else:
            i = idx
            if num == -1:
                while min_heap and checked[i] == 0:
                    _, i = heapq.heappop(min_heap)
                checked[i] = 0

            else:
                while max_heap and checked[i] == 0:
                    _, i = heapq.heappop(max_heap)
                checked[i] = 0

    if sum(checked) == 0:
        print('EMPTY')
    else:
        i = -1
        while i < 0 or checked[i] == 0:
            res1, i = heapq.heappop(max_heap)
            res1 *= -1
        i = -1
        while i < 0 or checked[i] == 0:
            res2, i = heapq.heappop(min_heap)
        print(res1, res2)