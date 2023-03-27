import heapq

def is_valid(N, x, y):
    '''
    helper function that return True, if x, y is valid position
    '''

    return 0 <= min(x, y) and max(x, y) < N

def competitive_plague(N, K, virus, S, X, Y):
    '''
    function that return the virus in position (X, Y) after S-seconds
    '''

    # if it already has virus
    if virus[X][Y]:
        return virus[X][Y]

    # starting from the center (X, Y)
    # in i-th step, consider the border whose element satisfies the following
    #               manhattan distance from (X, Y) == i
    for i in range(1, S+1):
        # initialize possible candidates
        # use it as minimum heapq using module heapq
        possible_candidates = []

        for dx in range(-i, i+1):
            pos_x = X + dx
            dy = i - abs(dx)
            # allowing multiplicity actually doesn't hurt in this case
            for pos_y in [Y-dy, Y+dy]:
                # if it's nonzero
                if is_valid(N, pos_x, pos_y) and virus[pos_x][pos_y]:
                    heapq.heappush(possible_candidates, virus[pos_x][pos_y])

        # if we have candidates, we don't need to proceed further
        # just return the minimum virus number among them
        if possible_candidates:
            return heapq.heappop(possible_candidates)

    # otherwise it's 0
    return 0


N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
print(competitive_plague(N, K, virus, S, X-1, Y-1))