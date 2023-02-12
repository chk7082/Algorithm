def allocation_of_seats(C, R, K):
    '''
    function that return the seat number of K-th waiting
    number in R by C seat matrix
    0, if not possible

    :param
    C (int) : range for x
    R (int) : range for y
    K (int) : waiting number

    :return
    (x, y), if possible
         0, otherwise
    '''

    # possibility check
    if K > C * R:
        return 0

    # initialize current position & possible actions
    cur_x = cur_y = 1
    cur_waiting_num = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    action_index = 0

    # initialize the matrix of size (C+2) by (R+2)
    # index 0 & C+1 for x : dummy
    # index 0 & R+1 for y : dummy
    not_visited = [[True] * (R+2) for _ in range(C+2)]
    for dummy_x in [0, C+1]:
        for y in range(R+2):
            not_visited[dummy_x][y] = False
    for dummy_y in [0, R+1]:
        for x in range(C+2):
            not_visited[x][dummy_y] = False
    not_visited[1][1] = False

    # until we meet query K
    while cur_waiting_num != K:
        # it always end, since K <= C * R by our condition
        if not_visited[cur_x + dx[action_index]][cur_y + dy[action_index]]:
            # update the state
            cur_x += dx[action_index]
            cur_y += dy[action_index]
            not_visited[cur_x][cur_y] = False
            cur_waiting_num += 1

        # if we can't move in current action direction, rotate
        else:
            action_index = (action_index + 1) % 4

    return cur_x, cur_y


C, R = map(int, input().split())
K = int(input())

# compute our result
result = allocation_of_seats(C, R, K)

if result == 0:
    print(0)
else:
    print(*result, sep=' ')