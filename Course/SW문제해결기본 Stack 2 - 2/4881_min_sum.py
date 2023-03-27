def min_sum(i, N, prev_sum):
    '''
    function that compute the minimum possible sum of N elements of N by N arr
    chosen by the following rules (recursively)
        rule - all elements should have different row/col index (resp.)

    :param
    i (int) : integer to denote that we have chosen i-many elements
    N (int) : integer representing the size of arr
    prev_sum (int) : sum of chosen i-many elements, just to discard some cases easily

    :return
    None, it just save it in variable min_sum_value
    '''

    # global variable to store min_sum_value
    global min_sum_value

    # if prev_sum already exceed(or at least equal to) the min_sum_value
    # we don't need to go further
    if prev_sum >= min_sum_value:
        return

    # if i == N & prev_sum < min_sum_value
    elif i == N:
        min_sum_value = prev_sum

    # otherwise, proceed
    else:
        next_candidates = [i for i in range(N) if col_usage[i]]

        # for each candidate
        for candidate in next_candidates:
            # since we have used it
            col_usage[candidate] = False

            # recursion step
            min_sum(i + 1, N, prev_sum + arr[i][candidate])

            # restore it
            col_usage[candidate] = True


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # whether to denote we could use that col index or not
    col_usage = [True] * N
    min_sum_value = 1e8

    # proceed recursion step
    min_sum(0, N, 0)

    print(f'#{t} {min_sum_value}')
