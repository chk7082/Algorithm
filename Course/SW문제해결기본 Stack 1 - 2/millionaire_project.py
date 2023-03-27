def millionaire_project(N, future):
    '''
    function that return the maximum profit of panic buying
    in the specified N-days of future

    :param
    N (int) : length of future list
    future (list) : future prices of product of N days

    :return
    result (int) : the maximum profit of panic buying
                   in the specified N-days of future
    '''

    # initialize our result
    # when we just stay
    result = 0

    # strategy : use maximum value in future
    #            before that maximum, buy all of them and sell it at the max
    #            now focus on the remaining ones on the right
    #            do the same procedure for that recursively

    # index to start finding maximum (going to update it in while loop)
    ind_to_start = 0
    while ind_to_start <= N-2:
        # compute the maximum
        max_val = max(future[ind_to_start:])
        # start index finding from ind_to_start
        # find index from the end (just to skip some, when multiplicity occurs)
        for i in range(N-1, ind_to_start - 1, -1):
            if future[i] == max_val:
                max_ind = i
                break

        # when we need to compute it
        if max_ind > ind_to_start:
            # from ind_to_start to max_ind - 1, compute the total summation of differences
            # we don't need to consider max_ind itself
            result += sum(map(lambda x: max_val-x, future[ind_to_start:max_ind]))

        # update ind_to_start
        ind_to_start = max_ind + 1

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    future = list(map(int, input().split()))
    print(f'#{t} {millionaire_project(N, future)}')