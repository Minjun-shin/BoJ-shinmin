N = int(input())
num_list = list(map(int, input().split()))

res = [0] * N
stack = []
mapping = {}

for i in range(N, 0, -1):
    curr = num_list[i-1]
    mapping[curr] = i - 1

    while stack and stack[-1] < curr:
        res[mapping[stack.pop()]] = i

    stack.append(curr)

print(*res)