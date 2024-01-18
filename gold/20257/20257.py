def DFS(n, result):
    global res
    if n == 4:
        valid = False
        for op in ops:
            valid = valid or op in result
        if eval(result) >= 0 and valid:
            res.add(eval(result))
        return
    
    if result and result[-1] not in ops:
        for op in ops:
            DFS(n, result+op)
    
    for i in range(4):
        if ch[i] == 0:
            ch[i] = 1
            DFS(n+1, result+num_list[i])
            ch[i] = 0


num_list = list(input().split())
ch = [0] * 4
ops = ['+', '-', '*']
res = set()
DFS(0, '')
print(len(res))