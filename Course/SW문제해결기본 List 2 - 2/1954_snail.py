def snail(N):
    '''
    function that return snail using N * N matrix
    with integers 1 ~ N^2 filled in clockwise direction

    :param
    N (int) : size of matrix

    :return
    snail_matrix (list) : 2-dim'l list representing N * N snail
    '''

    # initialize N * N matrix of boolean where each element
    # denote whether we visited that position before or not
    visited = [[False] * N for _ in range(N)]

    # initialize our resulting matrix with 1, just to consider initial point
    snail_matrix = [[1] * N for _ in range(N)]

    # define possible action (in clockwise order)
    # R D L U
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # initialize current position
    x = 0
    y = 0
    visited[0][0] = True

    # initialize action index (starts with Right direction) & current number
    action_index = 0
    cur_num = 2
    bound = N**2

    # until it exceed bound
    while cur_num <= bound:
        # new position
        new_x = x + dx[action_index]
        new_y = y + dy[action_index]

        # if it's valid position & not visited yet
        if validity(new_x, new_y, N) and (not visited[new_x][new_y]):
            # update it
            visited[new_x][new_y] = True
            x, y = new_x, new_y
            snail_matrix[new_x][new_y] = cur_num
            cur_num += 1
        # if it's not, rotate 90 degree in clockwise direction
        else:
            action_index = (action_index + 1) % 4

    return snail_matrix


def validity(x, y, N):
    '''
    function that determine whether (x,y) is valid position in N * N array or not

    :param
    (x, y) (tuple) : tuple containing position that we want to check validity
    N (int) : size of matrix

    :return:
    result (bool) : True, if valid
                    False, otherwise
    '''

    return max(x, y) <= N-1 and min(x, y) >= 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    snail_matrix = snail(N)
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(snail_matrix[i][j], end=' ')
        print()