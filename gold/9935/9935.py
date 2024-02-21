S = input().strip()
target = list(input().strip())
stack = []

for letter in S:
    stack.append(letter)
    if stack[-len(target):] == target:
        for _ in range(len(target)): stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')