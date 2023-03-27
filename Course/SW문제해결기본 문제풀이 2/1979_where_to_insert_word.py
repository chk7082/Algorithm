def where_to_insert_word(N, K, puzzle_arr):
    '''
    function that return the number of position
    where K-length word can exactly get in (in this word puzzle)

    :param
    N (int) : size of puzzle_arr (N by N)
    K (int) : length of word
    puzzle_arr (2-dim'l list) : N by N size matrix with
                                1, where word can get in
                                0, where word can't get in

    :return
    counts (int) : the number of position
                   where K-length word can exactly get in
    '''

    # initialize counts
    counts = 0

    # for each possible starting positions
    for i in range(N):
        for j in range(N - K + 1):
            # position (i, j) & horizontal word
            # if the region is all 1 & we can't extend it anymore
            if all(puzzle_arr[i][j:j+K]) and oor_or_0(i, j-1, N, puzzle_arr) and oor_or_0(i, j+K, N, puzzle_arr):
                counts += 1

            # position (j, i) & vertical word
            # if the region is all 1 & we can't extend it anymore
            if all([puzzle_arr[p][i] for p in range(j, j+K)]) and oor_or_0(j-1, i, N, puzzle_arr) and oor_or_0(j+K, i, N, puzzle_arr):
                counts += 1

    return counts


def oor_or_0(x, y, N, puzzle_arr):
    '''
    (out of range or 0)
    function that return
        True, if (x, y) -> out of range or puzzle_arr[x][y] == 0
        False, otherwise
    '''

    # the order in or operation matter
    return max(x, y) >= N or min(x, y) < 0 or (not puzzle_arr[x][y])


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {where_to_insert_word(N, K, puzzle_arr)}')