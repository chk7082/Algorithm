def max_diff(arr):
    '''
    function that computes maximum difference of two elements in arr

    :param
    arr (list) : list of positive integers

    :return:
    result (int) : maximum differnences of two elements in arr
                   (two elements might be the same one)
                   (i.e = maximum - minimum)
    '''

    # initialize our tracking
    # we don't need to keep tracking of corresponding index
    max_val, min_val = arr[0], arr[0]

    # subtle detail
    if len(arr) == 1:
        return 0

    # for each number in arr
    for num in arr[1:]:
        # if num is greater than current max_val
        if num > max_val:
            # update it
            max_val = num

        # if num is less than current min_val
        if num < min_val:
            # update it
            min_val = num

    return max_val - min_val

def interval_sum(arr, N, M):
    '''
    function that return the list containing all
    M-consecutive interval_sum of arr

    :param
    arr (list) : list of integers
    N (int) : length of arr
    M (int) : positive integer that represents
              consecutive length of interval sum

    :return:
    result (list) : list of integers containing all possible
                    M-consecutive interval sum (in original order)
    '''

    # compute cumulative sum first (iteratively)
    cum_sum = []

    # for each num in array
    cur_sum = 0
    for num in arr:
        cur_sum += num
        cum_sum.append(cur_sum)

    # return our wanted interval_sum
    # include the first term cum_sum[M-1]
    return [cum_sum[M-1]] + [y-x for x, y in zip(cum_sum[:N-M], cum_sum[M:])]

# T : number of test cases
T = int(input())

# for each test case
for t in range(1, T+1):
    # N, M
    N, M = map(int, input().split())

    # current test array
    t_arr = list(map(int, input().split()))

    print(f'#{t} {max_diff(interval_sum(t_arr, N, M))}')