def subset(arr):
    '''
    function that return 1, if there exists a nonempty subset of arr, sum up to 0
                         0, otherwise

    :param
    arr (list) : 1-dim'l list of integers

    :return:
    result (int) : 1, if there exists a nonempty subset of arr, sum up to 0
                   0, otherwise
    '''

    # N : length of arr
    N = len(arr)

    # for each subset of arr (using bit operation)
    # i starts from 1 (to avoid empty set)
    for i in range(1, 1<<N):
        # initialize current partial sum
        cur_sum = 0
        # use bits of i to determine whether each element of arr belongs to
        # current subset or not
        for j in range(N):
            # if j-th bit of i == 1
            if i & (1<<j):
                cur_sum += arr[j]

        # check if cur_sum == 0
        if (not cur_sum):
            return 1
    else: # for-else, if there's no such subset
        return 0

# number of test cases
T = int(input())

# for each test case
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{t} {subset(arr)}')