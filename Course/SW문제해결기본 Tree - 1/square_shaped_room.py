def square_shaped_room(N, arr):
    '''
    function that return the room number that maximize the number of
    possible consecutive move + 1 (& corresponding number of move + 1)
    (each move should increase the room number by exactly 1)

    :param
    N (int) : integer that represents the size of arr
    arr (list) : matrix (2-dim'l) of size (N+2) by (N+2)
                 with border filled with -1
                 & interior part filled with 1 ~ N^2

    :return
    (room_number, move + 1) (tuple) : tuple containing our wanted room number
                                      & corresponding move + 1
    '''

    # initialize our visited arr & stack
    can_visit = [[False]*(N+2)] + [[False] + [True]*N + [False] for _ in range(N)] + [[False]*(N+2)]
    stack = []

    # index : room value - element : (number of corresponding move) + 1
    # index 0 : dummy
    room_to_move = [0] * (N * N + 1)

    # define possible actions
    # L R U D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # for each point in grid
    for i in range(1, N+1):
        for j in range(1, N+1):
            # if we hadn't visited there yet,
            if can_visit[i][j]:
                # initialize point
                x, y = i, j

                # step 1. root finding step
                # root : the point where there's no adjacent neighbor which
                # has value 1 less than itself
                while True:
                    for action_index in range(4):
                        new_x = x + dx[action_index]
                        new_y = y + dy[action_index]
                        # if it has such neighbor
                        # we don't need to check if we had visited there or not
                        if arr[new_x][new_y] == arr[x][y] - 1:
                            x, y = new_x, new_y
                            break
                    # for-else, if x, y itself is such root
                    else:
                        break

                # now x, y is such root point
                # step 2. for each trace, record all info. in that trace
                stack.append((x, y))
                while True:
                    # we don't need to check if we had visited there or not
                    for action_index in range(4):
                        new_x = x + dx[action_index]
                        new_y = y + dy[action_index]
                        # if we have neighbor with value increase by 1
                        if arr[new_x][new_y] == arr[x][y] + 1:
                            x, y = new_x, new_y
                            stack.append((x, y))
                            break
                    # for-else, if it's the end point
                    else:
                        break

                # step 3. record the corresponding move + 1 for each positions
                #         using stack
                for k in range(1, len(stack) + 1):
                    x, y = stack.pop()
                    can_visit[x][y] = False
                    room_to_move[arr[x][y]] = k

    # return our result
    max_val = max(room_to_move)
    max_ind = room_to_move.index(max_val)

    return max_ind, max_val


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[-1] * (N+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]

    result = square_shaped_room(N, arr)
    print(f'#{t} {result[0]} {result[1]}')




