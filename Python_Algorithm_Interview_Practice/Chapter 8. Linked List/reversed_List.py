class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reversed_List(node, L):
    '''
    function that return reversed version of arr (Linked List of length L)
    '''

    # initialize it
    prev, node = node, node.next

    # change the linkage direction
    while node.next:
        next, node.next = node.next, prev

        # update it for next iteration
        node, prev = next, node

    node.next = prev

    # cumulate it
    result = []
    for _ in range(L-1):
        result.append(node.val)
        node = node.next

    result.append(node.val)

    return '->'.join(result)


arr = '1->2->3->4->5->NULL'.split('->')

# save it in ListNode
Linked_List = ListNode(arr[0])
node = Linked_List
for element in arr[1:-1]:
    node.next = ListNode(element)
    node = node.next

print(reversed_List(Linked_List, 5) + '->NULL')


