N = int(input())
num_list = list(map(int, input().split()))[::-1]

stack = []
curr = 1

while num_list:
    if num_list[-1] == curr:
        num_list.pop()
        curr += 1
    elif stack and stack[-1] == curr:
        stack.pop()
        curr += 1
    else:
        stack.append(num_list.pop())
        
while stack:
    if stack[-1] == curr:
        stack.pop()
        curr += 1
    else:
        break
        
if curr == N + 1:
    print('Nice')
else:
    print('Sad')