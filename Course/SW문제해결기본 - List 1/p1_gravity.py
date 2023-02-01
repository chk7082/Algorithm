# Gravity

# We don't need to rotate it actually
# just change the direction of gravity

def Gravity(arr):
    '''
    function that compute the maximum falling distance

    :param
    arr (list) : list of integers containing piled height of each columns

    :return:
    result (int) : maximum falling distance
    '''

    # Note that we only need to consider the top box of each column
    # (just by using the monotone property of each col)
    # Also note that if we've already considered falling distance of
    # (i,j) position, then we don't need to consider all the
    # lower right part of it (just because of similar reason)

    # using above analysis, we're gonna collect possible candidates
    candidate = []

    # starts with max_index
    cur_max = max(arr)
    cur_ind = arr.index(cur_max)


    while True:
        # compute how many piles on the right has lower height than itself
        # it is equivalent to calculating falling distance of that top one
        cur_top_falling_dist = sum(map(lambda x: x < cur_max, arr[cur_ind:]))

        # append it to possible candidate
        candidate.append(cur_top_falling_dist)

        # breaking condition , when there is no left region
        if cur_ind == 0:
            break

        # update new cur_max & cur_ind for left region (arr[:cur_ind])
        cur_max = max(arr[:cur_ind])
        cur_ind = arr.index(cur_max)

    # just return the maximum value of possible candidates
    return max(candidate)

# T = number of test cases
T = int(input())

# for each test case
for t in range(1, T+1):
    # we don't need to store length information
    _ = int(input())

    # input list for each test case
    t_arr = list(map(int, input().split()))

    # print our wanted result
    print(f'#{t} {Gravity(t_arr)}')



