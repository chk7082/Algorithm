def find_representative(v):
    '''
    function that return the representative of disjoint set containing v
    '''
    while v != representative[v]:
        v = representative[v]
    return v


def union(u_rep, v_rep):
    '''
    function that merge the 2 sets, one containing u, and the other containing v
    '''

    representative[v_rep] = u_rep


def divide_groups(N, M, submission, representative):
    '''
    function that return the number of disjoint sets reduced by submission
    '''

    # initialize our result
    # excluding index 0
    result = N

    # for each union query
    for u, v in zip(submission[::2], submission[1::2]):
        # find their representative
        # to figure out those two are in the same set or not
        u_rep = find_representative(u)
        v_rep = find_representative(v)

        # if we need to union them
        if u_rep != v_rep:
            result -= 1
            union(u_rep, v_rep)

    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    submission = list(map(int, input().split()))

    # make initial disjoint sets
    # index 0 : dummy
    representative = [i for i in range(N+1)]

    print(f'#{t} {divide_groups(N, M, submission, representative)}')

