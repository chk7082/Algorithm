def fly_extermination_3(N, M, flies):
    '''
    function that return the maximum number of flies that we could kill
    with one swing of fly swatter

    :param
    N (int) : positive integer representing the size of flies
    M (int) : positive integer representing the killing radius of fly swatter
    flies (list) : matrix (2-dim'l list) of size (N+2*M-2) by (N+2*M-2)
                   containing the number of flies in that region
                   (border : filled with 0, just for convenience)

    :return
    result (int) : the maximum number of flies that we could kill
                   with one swing of fly swatter
    '''

    # we're going to cumulate the result in this N by N matrix
    cumulation_plus = [flies[i][M-1:N+M-1] for i in range(M-1, N+M-1)]
    cumulation_x = [flies[i][M-1:N+M-1] for i in range(M-1, N+M-1)]

    # define actions
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for action_index in (1, 3, 4, 6):
        for i in range(N):
            for j in range(N):
                for step_size in range(1, M):
                    cumulation_plus[i][j] += flies[i+M-1+step_size*dx[action_index]][j+M-1+step_size*dy[action_index]]

    for action_index in (0, 2, 5, 7):
        for i in range(N):
            for j in range(N):
                for step_size in range(1, M):
                    cumulation_x[i][j] += flies[i+M-1+step_size*dx[action_index]][j+M-1+step_size*dy[action_index]]

    return max(max(map(max, cumulation_plus)), max(map(max, cumulation_x)))


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    flies = [[0]*(N+2*M-2)]*(M-1) + \
            [[0]*(M-1) + list(map(int, input().split())) + [0]*(M-1) for _ in range(N)] + \
            [[0]*(N+2*M-2)]*(M-1)

    print(f'#{t} {fly_extermination_3(N, M, flies)}')