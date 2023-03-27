def good_view(arr, N):
    '''
    function that computes the number of houses
    having good view
    (good view : the house which has no
    adjacent (distance <= 2) house in same altitude)

    (in leftmost(also rightmost) 2 regions, there is no building)

    :param
    arr (list) : list of
    N (int) : width of land including leftmost & rightmost 2 regions

    :return:
    result (int) : the number of houses having good view
    '''

    # initialize it
    result = 0

    # for each land with possible building
    for i in range(2, N-2):
        # add the # of houses which has good view in that land(col)

        # current height
        cur_height = arr[i]

        # max height among neighbors (land(column) with distance <= 2)
        max_neighbor_height = max(arr[i-2:i] + arr[i+1:i+3])

        # if there is neighborhood which is
        # taller than(or equal to) itself,
        # no good view house on that building
        # so we only need to consider opposite cases
        if max_neighbor_height < cur_height:
            # add good view house on current building
            result += cur_height - max_neighbor_height

    # return total # of good view house
    return result





# T : number of test cases
T = 10

# for each test cases
for t in range(1, T+1):
    # N
    N = int(input())

    # test array
    t_arr = list(map(int, input().split()))

    # print result
    print(f'#{t} {good_view(t_arr, N)}')