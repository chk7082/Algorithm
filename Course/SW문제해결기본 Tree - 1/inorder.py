class ListNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(tree, node):
    '''
    function that record inorder traversal path in array path

    :param
    tree (dict) : dictionary containing the ListNode of linked list
                  (which represents the tree)
    node (int) : node we're currently looking at
    '''

    # if node == None, just return
    if node is None:
        return

    inorder(tree, tree[node].left)
    path.append(node)
    inorder(tree, tree[node].right)


V = int(input())
E = V - 1 # since it's tree

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

path = []
inorder(tree, min(tree.keys()))
print(path)