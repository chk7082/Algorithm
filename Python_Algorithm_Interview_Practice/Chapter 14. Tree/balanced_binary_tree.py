class Solver:
    '''
    class that will give us the result
    '''
    def __init__(self, tree):
        '''
        define useful instance variable
        '''
        self.tree = tree
        self.length = len(tree) - 1
        self.result = True

    def balanced_binary_tree(self, node):
        '''
        function that return True, if the given tree is balanced
                            False, otherwise

        :param
        node (int) : current node we're interested in
        '''

        # if it's the end of tree
        if node > self.length or self.tree[node] is None:
            return 0

        else:
            # left node
            left_height = self.balanced_binary_tree(2 * node)

            # right node
            right_height = self.balanced_binary_tree(2 * node + 1)

            # if it's not balanced
            if abs(left_height - right_height) >= 2:
                self.result = False

            return max(left_height, right_height) + 1




tree1 = [None, 3, 9, 20, None, None, 15, 7]
L1 = len(tree1)
tree1_solver = Solver(tree1)
tree1_solver.balanced_binary_tree(1)
print(tree1_solver.result)

tree2 = [None, 1, 2, 2, 3, 3, None, None, 4, 4]
L2 = len(tree2)
tree2_solver = Solver(tree2)
tree2_solver.balanced_binary_tree(1)
print(tree2_solver.result)