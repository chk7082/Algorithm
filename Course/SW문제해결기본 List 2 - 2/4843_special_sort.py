def special_sort(N, arr):
    '''
    function that specially sorts arr internally
    (specially sorted : sort it with 1st max, 1st min, 2nd max, 2nd min, ...)

    :param
    N (int) : number of integers in arr
    arr (list) : list of integers that we want to sort specially

    :return
    None, it overwrite the original arr
    '''

    # Idea : use step in selection sort
    # whether to use max_finder or min_finder
    max_mode = True

    # don't need to do this when i = N - 1
    for i in range(N-1):
        if max_mode:
            # find maximum & swap it
            max_val, max_index = max_finder(arr[i:], i)
            arr[i], arr[max_index] = max_val, arr[i]
        else: # min_mode
            # find minimum & swap it
            min_val, min_index = min_finder(arr[i:], i)
            arr[i], arr[min_index] = min_val, arr[i]

        # change mode (for next iteration)
        max_mode = (not max_mode)


def max_finder(arr, start):
    '''
    function that return maximum element & corresponding index of arr

    :param
    arr (list) : arr that we want to find maximum & its index

    :return:
    (max_val, max_index) (tuple) : tuple containing what we wanted
    '''

    # initialize it
    max_val = -1e6
    max_index = -1

    for (i, num) in enumerate(arr):
        if num > max_val:
            max_val = num
            max_index = i

    return (max_val, max_index + start)


def min_finder(arr, start):
    '''
    just the oppositie of max_finder, refer max_finder
    '''

    # initialize it
    min_val = 1e6
    min_index = -1

    for (i, num) in enumerate(arr):
        if num < min_val:
            min_val = num
            min_index = i

    return (min_val, min_index + start)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # since we only print it up to 10th element,
    # it is sufficient to let min(N, 11)
    special_sort(min(N, 11), arr)

    print(f'#{t} ', end='')
    if N < 11:
        for num in arr:
            print(num, end=' ')
    else:
        for i in range(10):
            print(arr[i], end=' ')
    print()