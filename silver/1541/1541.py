def DFS(n, result, minus_state):
    global res
    if n == N-1:
        res = min(res, result)
        return
    
    if minus_state:
        if plus_minus[n] == '-':
            DFS(n+1, result + num_list[n+1], True)
            DFS(n+1, result + num_list[n+1], False)

        else:
            DFS(n+1, result - num_list[n+1], True)
            DFS(n+1, result - num_list[n+1], False)

    else:
        if plus_minus[n] == '-':
            DFS(n+1, result - num_list[n+1], True)
            DFS(n+1, result - num_list[n+1], False)

        else:
            DFS(n+1, result + num_list[n+1], False)


s = input()
num_list = list(map(int, s.replace('-', '+').split('+')))
plus_minus = [letter for letter in s if not letter.isdecimal()]
N = len(num_list)

res = float('inf')
DFS(0, num_list[0], False)
print(res)