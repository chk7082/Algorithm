def merge_two_binary_tree(tree1, tree2):
    '''
    function that merge two trees
    '''

    return list(map(element_wise_addition, zip(tree1, tree2)))


def element_wise_addition(num):
    '''
    helper function that return num1 + num2
    (if both of them is None -> return None
     if only one of them is None -> regard it as 0)
    '''

    if num[0] is None and num[1] is None:
        return None
    elif num[0] is None:
        return num[1]
    elif num[1] is None:
        return num[0]
    else:
        return num[0] + num[1]


tree1 = [None, 1, 3, 2, 5]
tree2 = [None, 2, 1, 3, None, 4, None, 7]

L1, L2 = len(tree1), len(tree2)
tree1 = tree1 + [None] * max(0, L2 - L1)
tree2 = tree2 + [None] * max(0, L1 - L2)

print(merge_two_binary_tree(tree1, tree2))