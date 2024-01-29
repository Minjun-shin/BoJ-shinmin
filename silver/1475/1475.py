num = input()
num_dict = {i:0 for i in range(0, 9)}

for letter in num:
    if letter == '9':
        num_dict[6] += 1
    else:
        num_dict[int(letter)] += 1

res = 0
for n in num_dict:
    if n == 6:
        res = max(res, (num_dict[n] + 1) // 2)
    else:
        res = max(res, num_dict[n])

print(res)