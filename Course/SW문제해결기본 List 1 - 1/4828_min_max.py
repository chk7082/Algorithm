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


# T : number of test cases
T = int(input())

# for each test case
for t in range(1, T+1):
    # we don't need to store length of it
    _ = int(input())

    # current test array
    t_arr = list(map(int, input().split()))

    print(f'#{t} {max_diff(t_arr)}')
