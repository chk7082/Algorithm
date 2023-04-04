def minimum_moving_distance(N, E, edges, D, not_yet, start, end):
    '''
    function that return the minimum distance from start to end
    '''

    while True:
        min_w = 1e9
        such_v = -1

        # find the next vertex that we want to confirm
        for v, w in enumerate(D):
            # position with distance 0 => confirmed already
            if not_yet[v] and w < min_w:
                min_w = w
                such_v = v

        # if it's our target, then done
        if such_v == end:
            return min_w

        # otherwise, we need to go further
        not_yet[such_v] = False  # confirm it
        for new_e, new_w in edges[such_v]:
            # update it
            D[new_e] = min(D[new_e], D[such_v] + new_w)


INF = 1e8
T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())

    start = 0
    end = N

    edges = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges[s].append((e, w))

    D = [INF] * (N+1)
    D[start] = 0
    for e, w in edges[start]:
        D[e] = w

    not_yet = [True]*(N+1)
    not_yet[start] = False

    print(f'#{t} {minimum_moving_distance(N, E, edges, D, not_yet, start, end)}')

