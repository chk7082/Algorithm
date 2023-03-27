def paper(max_N):
    '''
    function that solves the recursive formula up to max_N
    recurrence formula:
        f(n) = f(n-1) + 2 * f(n-2), with f(1) = 1, f(2) = 3
        (up to max_N)

    don't return, just save it on memoization array

    :param
    max_N (int) : maximum value of n we're interested in

    :return:
    memoization (list) : list of length (max_N + 1) where index i denote f(i)
                         index 0 -> dummy
    '''

    # index i for the result when N = 10 * i
    memoization = [0] * (max_N + 1)
    memoization[1] = 1
    memoization[2] = 3

    # compute it by recursive formula
    for i in range(3, max_N + 1):
        memoization[i] = memoization[i-1] + 2 * memoization[i-2]

    return memoization


T = int(input())
N_list = [int(input())//10 for _ in range(T)]
max_N = max(N_list)
max_N = max(3, max_N) # just to guarantee that max_N >= 3

# precompute recursive formula
memoization = paper(max_N)

for t in range(1, T+1):
    print(f'#{t} {memoization[N_list[t-1]]}')
