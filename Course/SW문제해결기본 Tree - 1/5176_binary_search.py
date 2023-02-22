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


T = int(input())
for t in range(1, T+1):
    V = int(input())
    # index 0 : dummy
    tree = list(range(V+1))

    path = []
    inorder(tree, 1, V)
    print(f"#{t} {path.index(1) + 1} {path.index(V//2) + 1}")


