def one_step_of_reversi(N, board, x, y, color):
    '''
    function that proceed one step of reversi game

    :param
    N (int) : integer representing the size of board
    board (list) : N by N matrix(2-dim'l list)
                   where element 0, means there's nothing
                                 nonzero, means there is stone (1 or 2)
    x, y (int) : position that we want to put color stone
    color (int) : 1 if the stone is black,
                  2 if white

    :return:
    None, it changes board internally
    '''

    # define possible actions
    # L R U D & LL LR UL UR
    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]

    # for each action (direction)
    for action_index in range(8):
        new_x, new_y = x + dx[action_index], y + dy[action_index]

        # the another color
        another_color = 3 - color

        while board[new_x][new_y] == another_color:
            # move as possible as it can
            new_x += dx[action_index]
            new_y += dy[action_index]

        # (new_x, new_y) : the position that is not in the another_color for the first time
        # if its original color -> apply reversi rule
        if board[new_x][new_y] == color:
            # if it was moving vertically
            if action_index in [2, 3]:
                for i in range(x, new_x, dx[action_index]):
                    board[i][y] = color
            # if it was moving horizontally
            elif action_index in [0, 1]:
                for i in range(y, new_y, dy[action_index]):
                    board[x][i] = color
            # if it was moving diagonally
            else:
                for i, j in zip(range(x, new_x, dx[action_index]), range(y, new_y, dy[action_index])):
                    board[i][j] = color


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    # initialize our game board
    # 0 to the border
    board = [[0]*(N+2) for _ in range(N+2)]
    middle_left_index = (N+1)//2
    board[middle_left_index][middle_left_index] = 2
    board[middle_left_index + 1][middle_left_index + 1] = 2
    board[middle_left_index][middle_left_index + 1] = 1
    board[middle_left_index + 1][middle_left_index] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        # proceed one step
        one_step_of_reversi(N, board, x, y, color)

    # compute the number of black/white stones (resp.)
    num_of_black_stones = 0
    num_of_white_stones = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                num_of_black_stones += 1
            elif board[i][j] == 2:
                num_of_white_stones += 1

    print(f'#{t} {num_of_black_stones} {num_of_white_stones}')


