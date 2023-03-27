def jingi_bread_store(N, M, K, customer):
    '''
    function that return 'Possible', if jingi can give bread to all customers without waiting
                       'Impossible', otherwise

    :param
    N (int) : the number of customer today
    M (int) : the amount of time(second) to make K bread
    K (int) : the amount of bread could be made after M seconds
    customer (list) : the list containing the arrival time for each N customers

    :return
    result (str) : 'Possible', if jingi can give bread to all customers without waiting
                 'Impossible', otherwise
    '''

    # sort the customer (in increasing order)
    customer_sorted = sorted(customer)

    # check for each customer sequentially
    # given to store the number of previously given bread
    # since customer_sorted : sorted in increasing order
    # we could just determine whether it's possible or not
    # by only the given & time below

    for given, time in enumerate(customer_sorted):
        total_bread_can_be_made_until_now = (time // M) * K

        # since we need (given + 1) - many bread until now
        if total_bread_can_be_made_until_now <= given:
            return 'Impossible'

    # for - else
    else:
        return 'Possible'


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())

    customer = list(map(int, input().split()))

    print(f'#{t} {jingi_bread_store(N, M, K, customer)}')
