def inorder(tree, v, V):
    '''
    function that record inorder traversal path in array path
    :param
    tree (list) : list containing the data of each node
    v (int) : node we're currently looking at
    V (int) : total number of vertices
    '''

    # inorder
    # left node : 2 * v
    # right node : 2 * v + 1

    global cur_sum

    doubled = 2 * v
    if doubled <= V and not (tree[doubled] is None):
        inorder(tree, doubled, V)

    tree[v], cur_sum = cur_sum, cur_sum - tree[v]

    if doubled <= V - 1 and not (tree[doubled + 1] is None):
        inorder(tree, doubled + 1, V)


tree = [None, 4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
cur_sum = sum([num for num in tree if not (num is None)])

inorder(tree, 1, len(tree) - 1)
print(tree)
