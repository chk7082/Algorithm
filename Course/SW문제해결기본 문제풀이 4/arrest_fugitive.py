from collections import deque

def arrest_fugitive(N, M, R, C, L, tunnel):
    '''
    function that return the number of candidate area
    where the fugitive is possibly at (after L-hours elapsed since prison break)

    :param
    N, M (int) : integers representing the size of tunnel
    R, C (int) : integers representing the position of the manhole
    L (int) : the time elapsed since prison break
    tunnel (list) : matrix (2-dim'l list) of size N by M
                    whose element represent the type of pipe in that location

    :return
    result (int) : the number of candidate area where the fugitive
                   is possibly at (after L-hours elapsed since prison break)
    '''

    # initialize our result
    result = 0

    # define possible action
    # 3 - index -> index of reverse direction
    # L U D R
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]

    # initial point, queue
    q = deque([(R, C, 1)])

    # whether to denote if we can visit there or not
    can_visit = [[False]*(M+2)] + [[False] + [True]*M + [False] for _ in range(N)] + [[False]*(M+2)]
    can_visit[R][C] = False

    # BFS
    while q:
        x, y, dist = q.popleft()

        # if dist > L -> we don't need to proceed further
        if dist > L:
            break
        # if dist <= L
        else:
            # count the result
            result += 1

            # for each direction that the pipe is linked to
            for action_index in pipe_type[tunnel[x][y]]:
                new_x, new_y = x + dx[action_index], y + dy[action_index]

                # if we could go there
                if can_visit[new_x][new_y] and (3 - action_index) in pipe_type[tunnel[new_x][new_y]]:
                    q.append((new_x, new_y, dist + 1))
                    can_visit[new_x][new_y] = False

    return result


# for each pipe_type, record the direction that is opened to (w.r.t action)
pipe_type = [[],
             [0, 1, 2, 3],
             [1, 2],
             [0, 3],
             [1, 3],
             [2, 3],
             [0, 2],
             [0, 1]]

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    # -1 for border
    tunnel = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)]

    print(f'#{t} {arrest_fugitive(N, M, R + 1, C + 1, L, tunnel)}')
