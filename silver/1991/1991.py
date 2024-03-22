def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(node_dict[node]['left'])
        preorder(node_dict[node]['right'])


def inorder(node):
    if node != '.':
        inorder(node_dict[node]['left'])
        print(node, end='')
        inorder(node_dict[node]['right'])


def postorder(node):
    if node != '.':
        postorder(node_dict[node]['left'])
        postorder(node_dict[node]['right'])
        print(node, end='')


N = int(input())
node_dict = {}

for _ in range(N):
    root, left, right = input().split()
    node_dict[root] = {'left':left, 'right':right}

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()