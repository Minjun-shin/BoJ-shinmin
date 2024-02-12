S = input().strip()
stack = []

for letter in S:
    if letter in ['(', '[']:
        stack.append(letter)

    elif letter == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(2)

        elif len(stack) >= 2 and str(stack[-1]).isdecimal() and stack[-2] == '(':
            tmp = stack.pop()
            stack.pop()
            stack.append(2*tmp)

        else:
            print(0)
            break

        if len(stack) >= 2 and str(stack[-1]).isdecimal() and str(stack[-2]).isdecimal():
            stack.append(stack.pop() + stack.pop())

    elif letter == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            stack.append(3)

        elif len(stack) >= 2 and str(stack[-1]).isdecimal() and stack[-2] == '[':
            tmp = stack.pop()
            stack.pop()
            stack.append(3*tmp)

        else:
            print(0)
            break

        if len(stack) >= 2 and str(stack[-1]).isdecimal() and str(stack[-2]).isdecimal():
            stack.append(stack.pop() + stack.pop())

else:
    if len(stack) == 1 and str(stack[-1]).isdecimal():
        print(stack[0])
    else:
        print(0)