def building_airstrip(N, X, altitude):
    '''
    function that return the possible number of airstrip on this land
    with given latitude

    :param
    N (int) : size of the land
    X (int) : length of the airstrip
    altitude (list) : matrix (2-dim'l list) containing the altitude of each position
    '''

    # initialize our object
    result = 0

    # for each row
    for row in altitude:
        result += helper_function(N, X, row)

    # for each column
    for col in zip(*altitude):
        result += helper_function(N, X, col)

    return result


def helper_function(N, X, line):
    '''
    function that return 1, if the given line(row/col) can be used as airstrip
                         0, otherwise
    '''

    # initialize the array that will contain whether there's a airstrip in that position
    without_airstrip = [True] * N

    prev = 0
    for cur in range(1, N):
        diff = line[cur] - line[prev]

        # abs value of height difference should be bounded by 1
        if abs(diff) >= 2:
            return 0

        # elif diff == 0:
        #     pass

        # if the increment of height is 1
        elif diff == 1:
            # our interest
            interest = range(prev-X+1, prev+1)

            if is_possible(N, X, line, interest, without_airstrip):
                # build airstrip
                pass
            else:
                return 0

        elif diff == -1:
            # our interest
            interest = range(cur, cur+X)

            if is_possible(N, X, line, interest, without_airstrip):
                # build airstrip
                pass
            else:
                return 0

        # update prev
        prev += 1

    # if we can build airstrip in that line
    return 1


def is_possible(N, X, line, interest, without_airstrip):
    '''
    function that return True if we could build slope to our interest
    '''

    # out of range
    if interest[0] < 0 or interest[-1] >= N:
        return False

    # check if there's already slope
    for i in interest:
        if not without_airstrip[i]:
            return False

    # check if it's flat
    height = line[interest[0]]

    for i in interest[1:]:
        if line[i] != height:
            return False

    # otherwise it's valid
    # build slope in there
    for i in interest:
        without_airstrip[i] = False

    return True


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    altitude = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {building_airstrip(N, X, altitude)}')


