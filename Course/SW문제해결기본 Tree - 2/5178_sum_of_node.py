def sum_of_node(N, i):
    '''
    function that fill in the values of the remaining non-leaf node in tree

    :param
    N (int) : total number of vertices in tree
    i (int) : current vertex that we're looking at
    '''

    # use postorder traversal
    if i > N:
        return 0
    # if it's nonzero (predetermined)
    elif tree[i]:
        return tree[i]
    # otherwise
    else:
        left_value = sum_of_node(N, 2*i)
        right_value = sum_of_node(N, 2*i + 1)

        # use those two to determine the value of current node
        tree[i] = left_value + right_value

        return tree[i]


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        leaf_node, value = map(int, input().split())
        tree[leaf_node] = value

    sum_of_node(N, 1)

    print(f'#{t} {tree[L]}')

