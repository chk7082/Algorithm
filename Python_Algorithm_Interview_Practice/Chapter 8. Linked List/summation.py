class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __add__(self, other):
        return summation(self, other)


def summation(Node1, Node2):
    '''
    function that compute the summation of two integers represented
    as a Linked List (in reversed order)

    :param
    Node1, Node2 (ListNode) : first position of each integer
                              in Linked List representation

    :return
    result (ListNode) : first position of summation of the two above
    '''

    # save original node (just to return it)
    original_node = Node1

    # element-wise addition of each digits
    while Node1:
        # update it
        Node1.val = Node1.val + Node2.val

        # if it's greater than 10
        if Node1.val >= 10:
            Node1.val %= 10
            # and if it's the end
            if not Node1.next:
                Node1.next = ListNode(1)
            else:
                Node1.next.val += 1

        # for the next digit
        Node1 = Node1.next
        Node2 = Node2.next

    return original_node


string = '(2->4->3)+(5->6->4)'
index = string.find(')')

# first & second part
list1 = list(map(int, string[1: index].split('->')))
list2 = list(map(int, string[index+3: -1].split('->')))

# initialize Node1 and Node2
Node1 = ListNode(list1[0])
Node2 = ListNode(list2[0])

# Linked List 1
temp_node = Node1

# Link the remaining ones
for element in list1[1:]:
    temp_node.next = ListNode(element)
    temp_node = temp_node.next

# Linked List 2
temp_node = Node2

# Link the remaining ones
for element in list2[1:]:
    temp_node.next = ListNode(element)
    temp_node = temp_node.next

# our result
Node3 = Node1 + Node2
result = []
for _ in range(len(list1)):
    result.append(Node3.val)
    Node3 = Node3.next

print('->'.join(map(str, result)))

