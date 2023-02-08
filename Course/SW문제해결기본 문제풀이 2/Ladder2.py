def ladder2(ladder_matrix):
    '''
    function that find the starting point which yield minimum distance
    in ladder game

    :param
    ladder_matrix (list) : 2-dim'l array of size N * N
                           representing ladder with 1/0

    :return
    result (int) : starting point which yield minimum distance
    '''

    # size of ladder_matrix
    N = 100

    # the set of possible starting points
    possible_start_pts = [j for (j, value) in enumerate(ladder_matrix[0])
                        if value]

    # length of possible_end_pts
    L = len(possible_start_pts)

    # counts the length w.r.t each end pt
    # since every path from each starting pt should go down (no up -> total N)
    # starts from there (precompute it)
    counts = [N] * L

    # since we're going to count all length at once,
    # we need to consider the order of after each swap (horizontal edge)
    cur_order = list(range(L))

    # column that we're interested in for figuring out if there's
    # horizontal edge or not
    # used possible_end_pts[:-1] just to exclude the last one
    interest_cols = [j+1 for j in possible_start_pts[:-1]]

    # for each row
    for row in range(N):
        # for each possible horizontal edge
        for idx, interest_col in enumerate(interest_cols):
            if ladder_matrix[row][interest_col]:
                # what we should do
                # swap the order (for those two order with this horizontal edge)
                # add length of horizontal edge (excluding vertical area) to both

                # add horizontal_length
                horizontal_length = possible_start_pts[idx + 1] - possible_start_pts[idx] - 1
                counts[cur_order[idx]] += horizontal_length
                counts[cur_order[idx+1]] += horizontal_length

                # swap the order
                cur_order[idx] , cur_order[idx+1] = cur_order[idx+1], cur_order[idx]

    min_start_idx = L
    min_distance = 1e6
    # find starting point which yield minimum distance (if tie, return larger point)
    for i in range(L-1, -1, -1):
        cur_distance = counts[i]
        # find it backward (just to consider tie case)
        if cur_distance < min_distance:
            min_distance = cur_distance
            min_start_idx = i

    return possible_start_pts[min_start_idx]




for _ in range(10):
    t = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{t} {ladder2(ladder_matrix)}')
