def calc(num):
    global res
    if not graphs[num]:
        res += 1
        return
    
    for new in graphs[num]:
        calc(new)


N = int(input())
num_list = list(map(int, input().split()))
D = int(input())
graphs = [[] for _ in range(N)]
state = True

for idx, num in enumerate(num_list):
    if idx == D and num == -1:
        state = False
        continue
    if idx == D or num == D:
        continue
    if num == -1:
        S = idx
        continue
    graphs[num].append(idx)

if state:
    res = 0
    calc(S)
    print(res)
else:
    print(0)