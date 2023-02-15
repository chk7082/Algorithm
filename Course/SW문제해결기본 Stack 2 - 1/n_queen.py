def n_queen(a, k, N):
    '''
    function that computes the number of cases that N-many queens can be placed
    in N by N chessboard s.t none of them can attack the others

    :param
    a (list) : current array info (ith element -> column index of queen in row i)
    k (int) : current length of a
    N (int) : size of chessboard & number of queens

    :return
    result (int) : the number of cases that N-many queens can be placed
                   in N by N chessboard s.t none of them can attack the others
    '''

    c = [0] * N

    # if it's valid queen placements
    if k == N:
        print(a)
        global result
        result += 1

    # not yet
    else:
        k += 1

        currently_forbidden = set()
        for pos in enumerate(a[:k]):
            # compute absolute value of vertical difference
            # it's totally okay for the elements in currently_forbidden set
            # to deviate from the designated range (0 ~ N-1)
            abs_ver_diff = abs(pos[0] - k)
            currently_forbidden.update([pos[1], pos[1] - abs_ver_diff, pos[1] + abs_ver_diff])

        candidates = []
        for i in range(N):
            # if that position is safe
            if not (i in currently_forbidden):
                a[k] = i
                n_queen(a, k, N)


result = 0

N = int(input())
k = -1
a = [0] * N
n_queen(a, k, N)
print(result)