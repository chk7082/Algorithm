def gobang(N, board):
    '''
    function that return YES, if there's consecutive 5 stones('o') in board
                          NO, otherwise

    :param
    N (int) : positive integer representing the size of board
    board (list) : list of strings representing the current state on board

    :return
    result (str) : YES, if there's consecutive 5 stones('o') in board
                    NO, otherwise
    '''

    # exhaustive search
    for i in range(4, N+4):
        for j in range(4, N+4):
            # if there's no stone in this position, just continue
            if board[i][j] == '.':
                continue

            # otherwise
            else:
                # horizontal check
                for step_size in range(1, 5):
                    if board[i+step_size][j] == '.':
                        break
                else:
                    return 'YES'

                # vertical check
                for step_size in range(1, 5):
                    if board[i][j+step_size] == '.':
                        break
                else:
                    return 'YES'

                # diagonal 1 (from upper left to lower right)
                for step_size in range(1, 5):
                    if board[i+step_size][j+step_size] == '.':
                        break
                else:
                    return 'YES'

                # diagonal 2 (from upper right to lower left)
                for step_size in range(1, 5):
                    if board[i+step_size][j-step_size] == '.':
                        break
                else:
                    return 'YES'

    return 'NO'


T = int(input())
for t in range(1, T+1):
    N = int(input())

    # border filled with '.' (width : 4)
    board = ['.'*(N+8)]*4 + ['....' + input() + '....' for _ in range(N)] + ['.'*(N+8)]*4

    print(f'#{t} {gobang(N, board)}')

