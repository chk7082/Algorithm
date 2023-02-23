def cube_root(N):
    '''
    function that compute the cube root of N

    :param
    N (int) : positive integer that we want to find cube root of it

    :return
    X (int) : cube root of N, if it's integer
                          -1, otherwise
    '''

    # since x^3 is increasing function w.r.t x
    # we could use binary search

    # initialize the range of candidate
    left, right = 1, N

    while left <= right:
        middle = (left + right) // 2
        mid_value = middle ** 3

        # if it's N -> done
        if mid_value == N:
            return middle
        # if it's greater than N
        elif mid_value > N:
            right = middle - 1
        # if it's less than N
        else:
            left = middle + 1

    return -1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t} {cube_root(N)}')