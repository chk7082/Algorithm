def sum_of_subset(N, K):
    '''
    function that return the number of subsets of [1,2,...,12],
    which has cardinality N & sums up to K

    :param
    N (int) : cardinality condition of subset
    K (int) : summation value that we want

    :return
    counts (int) : the number of subsets of [1,2,...,12],
                  which has exactly N elements & sums up to K
    '''
    # initialize our result
    counts = 0

    # when does we choose max element while maintaining validity?
    # choose 1 ~ N-1 & choose the highest one as possible as we can
    # then total summation -> N*(N-1)/2 + (the highest one)
    # (which should be equal to K)
    # so abandon all elements with value > K - N*(N-1)/2
    length = min(K - N*(N-1)//2, 12)
    arr = list(range(1, length + 1))

    # to deal with minor cases
    if length < N:
        return 0

    # for each combination of N-many subset of arr
    # check if it sums up to 1
    # for each i (subset instance)
    for i in range(1 << length):
        # check its j-th bit
        # whether to include j-th element of arr or not
        cur_sum = 0
        cur_cardinality = 0
        for j in range(length):
            if i & (1 << j):
                cur_cardinality += 1
                cur_sum += arr[j]

        # check if it meets the condition
        if cur_cardinality == N and cur_sum == K:
            counts += 1

    return counts

# number of test cases
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    print(f'#{t} {sum_of_subset(N, K)}')


