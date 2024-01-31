def mklist(num1, num2):
    res = [num1]

    while num2 >= 0:
        res.append(num2)
        num1, num2 = num2, num1-num2
    
    return res


N = int(input())
ans = (0, [])

for i in range(N, -1, -1):
    lst = mklist(N, i)
    if ans[0] <= len(lst):
        ans = (len(lst), lst)

    else:
        break

print(ans[0])
print(*ans[1])