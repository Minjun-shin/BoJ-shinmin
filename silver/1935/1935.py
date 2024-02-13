def calcpostfix(S):
    stack = []
    for letter in S:
        if letter.isalpha():
            stack.append(mapping[letter])

        else:
            b, a = stack.pop(), stack.pop()
            if letter == '+':
                stack.append(a+b)
            elif letter == '-':
                stack.append(a-b)
            elif letter == '*':
                stack.append(a*b)
            else:
                stack.append(a/b)
    
    return float(stack[-1])


N = int(input())
S = input().strip()
mapping = {chr(ord('A')+i):int(input()) for i in range(N)}

print(f"{calcpostfix(S):.2f}")