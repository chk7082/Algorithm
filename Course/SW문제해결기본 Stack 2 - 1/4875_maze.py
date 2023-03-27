def maze(N, maze_matrix):
    '''
    function that return 1, if there is a path from 2(in last row) to 3(in first row)
                         0, otherwise

    :param
    N (int) : size of maze_matrix
    maze_matrix (list) : 2-dim'l list of integers (N by N)
                         where 2 denote starting point,
                               3 denote end point,
                               1 denote the wall, (we can't move)
                               0 denote the path we could possible go through
                               (extended matrix, with 1 in border)

    :return
    result (int) : 1 if there is a path from 2(in last row) to 3(in first row)
    '''

    # initialize our starting & end position

    cur_x, cur_y = find_2_dim_index(N, maze_matrix, 2)
    end_x, end_y = find_2_dim_index(N, maze_matrix, 3)

    # define possible actions
    # L U R D
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    action_index = 0

    # initialize our stack
    # maze_matrix[cur_x][cur_y] is already nonzero, we don't need to update it
    stack = [(cur_x, cur_y)]

    # while stack is nonempty
    while stack:
        cur_x, cur_y = stack.pop()

        # for each action
        for action_index in range(4):
            new_x, new_y = cur_x + dx[action_index], cur_y + dy[action_index]

            # if it's the end point (3)
            if new_x == end_x and new_y == end_y:
                return 1

            # if we could go there (0)
            elif not maze_matrix[new_x][new_y]:
                # update it
                maze_matrix[new_x][new_y] = 1
                stack.append((new_x, new_y))

    # if the end point is not reachable
    return 0


def find_2_dim_index(N, matrix, target):
    '''
    function that return the 2-dim'l indices of target in matrix

    :param
    N (int) : integer representing the size of matrix
    matrix (list) : 2-dim'l array (N by N) containing at least 1 target element
    target (int) : target element that we want to find index

    :return
    (x, y) (tuple) : tuple containing 2-dim'l index
    '''

    for row_ind in range(N):
        try:
            col_ind = matrix[row_ind].index(target)

            # if we successfully find that, (i.e, col_ind is not -1)
            return row_ind, col_ind
        except:
            pass


T = int(input())
for t in range(1, T+1):
    N = int(input())

    # barricade
    maze_matrix = list(map(lambda array: [1]+array+[1], [list(map(int, list(input()))) for _ in range(N)]))
    maze_matrix = [[1] * (N + 2)] + maze_matrix + [[1]*(N+2)]

    print(f'#{t} {maze(N+2, maze_matrix)}')


