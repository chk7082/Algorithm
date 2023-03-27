def inorder(tree, v, V):
    '''
    function that record inorder traversal path in array path
    :param
    tree (list) : list containing the data of each node
    v (int) : node we're currently looking at
    V (int) : total number of vertices
    '''

    # inorder
    # since it's complete binary tree
    # left node : 2 * v
    # right node : 2 * v + 1
    doubled = 2 * v
    if doubled <= V:
        inorder(tree, doubled, V)
    path.append(tree[v])
    if doubled <= V - 1:
        inorder(tree, doubled + 1, V)


arr = [None, -10, -3, 0, 5, 9]
V = len(arr) - 1
path = []
inorder(list(range(V+1)), 1, V)

BST = [None] + [-1] * V
for i, index in enumerate(path, start=1):
    BST[index] = arr[i]

print(BST)