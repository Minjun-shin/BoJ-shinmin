Target = int(input())
curr = [64]
sum_num = 64

while sum_num > Target:
    num = curr.pop()
    curr.append(num // 2)
    if sum_num - num // 2 >= Target:
        sum_num -= num // 2

    else:
        curr.append(num // 2)

print(len(curr))