def ladder(ladder_matrix):
    '''
    function that return the corresponding starting point,
    given ladder matrix & end point

    :param
    ladder_matrix (list) : 2-dim'l array of size N * N
                           representing ladder with 1/0,
                           unique 2 in the final row denote the end point
                           that we want to find corresponding starting point

    :return
    result (int) : corresponding starting point in the first row
    '''

    # initialize useful constant
    N = 100

    # starts from the end point
    cur_x = N-1
    cur_y = ladder_matrix[-1].index(2)

    # whether to denote horizontal move is possible or not
    move_horizontally = True

    while True:
        # if it reaches the starting point
        # ending condition
        if cur_x == 0:
            return cur_y

        # when we have to go left
        if y_validity(cur_y - 1, N) and ladder_matrix[cur_x][cur_y - 1] and move_horizontally:
            # go left as far as we can
            move_horizontally = False
            while y_validity(cur_y - 1, N) and ladder_matrix[cur_x][cur_y - 1]:
                cur_y -= 1

        # when we have to go right
        elif y_validity(cur_y + 1, N) and ladder_matrix[cur_x][cur_y + 1] and move_horizontally:
            # go right as far as we can
            move_horizontally = False
            while y_validity(cur_y + 1, N) and ladder_matrix[cur_x][cur_y + 1]:
                cur_y += 1

        # when we have to go up
        else:
            move_horizontally = True
            cur_x -= 1


def y_validity(y, N):
    '''
    function that return True, if 0 <= y <= N-1
                         False, otherwise
    '''

    return 0 <= y <= N-1


for _ in range(10):
    t = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{t} {ladder(ladder_matrix)}')
