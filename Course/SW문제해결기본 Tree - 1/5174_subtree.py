class ListNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(tree, node):
    '''
    function that record preorder traversal path in array path

    :param
    tree (dict) : dictionary containing the ListNode of linked list
                  (which represents the tree)
    node (int) : node we're currently looking at
    '''

    # global variable sub_V
    global sub_V

    # if node == None, just return
    if node is None:
        return

    sub_V += 1
    preorder(tree, tree[node].left)
    preorder(tree, tree[node].right)


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())

    # initialize empty dictionary
    tree = dict()

    edges = list(map(int, input().split()))

    for parent, child in zip(edges[::2], edges[1::2]):
        # default setting
        tree.setdefault(parent, ListNode(parent))
        tree.setdefault(child, ListNode(child))

        # if left is empty
        if not tree[parent].left:
            tree[parent].left = child
        # else
        else:
            tree[parent].right = child

    # number of vertices in subtree (with root node : N)
    sub_V = 0
    preorder(tree, N)

    print(f'#{t} {sub_V}')
