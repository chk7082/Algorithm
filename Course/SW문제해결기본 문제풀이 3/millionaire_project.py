def millionaire_project_stack(N, future):
    '''
    function that return the maximum profit of panic buying
    in the specified N-days of future

    :param
    N (int) : length of future list
    future (list) : future prices of product of N days

    :return
    result (int) : the maximum profit of panic buying
                   in the specified N-days of future
    '''

    # initialize our result
    # when we just stay
    result = 0

    cur_max = future[N-1]

    # for each price from the last future
    # if it's bigger than future, update cur_max
    # if not buy it and resell at future cur_max price
    for i in range(N-2, -1, -1):
        if cur_max < future[i]:
            # update cur_max
            cur_max = future[i]
        else:
            # panic-buy it and resell that the cur_max (at future)
            result += cur_max - future[i]

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    future = list(map(int, input().split()))
    print(f'#{t} {millionaire_project_stack(N, future)}')