class ListNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def cal(tree, node):
    '''
    function that compute the expression represented as tree

    :param
    tree (dict) : dictionary containing the ListNode of linked list
                  (which represents the tree)
    node (int) : node we're currently looking at
    '''

    # if it's integer
    if type(tree[node].data) in (int, float):
        return tree[node].data
    # if it's string
    else:
        # use postorder traversal
        left_value = cal(tree, tree[node].left)
        right_value = cal(tree, tree[node].right)
        return operate(left_value, right_value, tree[node].data)


def operate(num1, num2, operator):
    '''
    function that return the result of {num1} {operator} {num2}
    '''

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2


T = 10
for t in range(1, T+1):
    N = int(input())

    # initialize empty dictionary
    tree = dict()

    for _ in range(N):
        node, *rest = input().split()
        node = int(node)

        if len(rest) == 1:
            tree[node] = ListNode(int(rest[0]))
        elif len(rest) == 3:
            operator = rest[0]
            tree[node] = ListNode(operator, left = int(rest[1]), right = int(rest[2]))

    print(f'#{t} {int(cal(tree, 1))}')
