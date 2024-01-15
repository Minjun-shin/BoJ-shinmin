N = int(input())
res = 0
for _ in range(N):
    s = input()
    bef = ''
    l_list = []
    
    for letter in s:
        if letter not in l_list:
            bef = letter
            l_list.append(letter)
        elif letter != bef:
            break
    
    else:
        res += 1

print(res)