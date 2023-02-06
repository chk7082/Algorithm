def delta1(arr, N):
    '''
    function that compute the total sum of sum_of_adjacent_abs_diff
    w.r.t each element in arr
    (where, sum_of_adjacent_abs_diff of element is the summation of
    absolute difference to its adjacent ones)

    :param
    arr (list) : given 2-dim'l (N by N) array
    N (int) : positive integer that represent the dimension of arr

    :return:
    result (num) : number that represent the total sum of sum_of_adjacent_abs_diff
    '''

    # initialize our result
    result = 0

    # initialize possible actions
    # L R U D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # for each element in arr
    for x in range(N):
        for y in range(N):
            # for each action in
            for i in range(len(dx)):
                # new_position
                new_x = x + dx[i]
                new_y = y + dy[i]

                # if (new_x, new_y) is valid position
                # then cumulate it
                if min(new_x, new_y) >= 0 and max(new_x, new_y) <= N-1:
                    result += abs(arr[new_x][new_y] - arr[x][y])

    return result

def delta2(arr, N):
    '''
    (simplified version)
    same as delta1
    '''

    result = 0

    for x in range(N):
        for y in range(N-1):
            result += 2 * abs(arr[x][y+1] - arr[x][y])

    for x in range(N-1):
        for y in range(N):
            result += 2 * abs(arr[x+1][y] - arr[x][y])

    return result


# number of test cases
T = int(input())

# choose whether to use delta1 or delta2
delta = delta2

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {delta(arr, N)}')


