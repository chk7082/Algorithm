def electric_bus(K, N, M, charge_arr):
    '''
    function that return minimum charge numbers to go to the end point,
    0 if the end point is not reachable

    :param
    K (int) : maximum moving distance after each charge
    N (int) : index number of the last bus stop (0~N -> total (N+1)-many)
    M (int) : number of charge stations
    charge_arr (list) : list of indices of charge stations
                        (assume it has already been sorted)

    :return
    count (int) : minimum charge numbers if the end point is reachable,
                   0 otherwise
    '''

    # total length of bus route : N+1

    # initialize our result and current positions
    count = 0
    cur_position = 0 # initial point

    # consider reachable range without any extra charge
    # (cur_position + 1) ~ (cur_position + K)
    # there should be another charge station or the end point
    # we're gonna use greedy algorithm
    # since it's always better to go as far as it can without charge

    while True:
        # if end point is in that range, end
        if cur_position + K >= N:
            return count
        # if not
        else:
            for charge_station in reversed(charge_arr):
                if cur_position + 1 <= charge_station <= cur_position + K:
                    # go to charge station as far as it can without charge
                    count += 1
                    cur_position = charge_station
                    break
            else: # if we don't meet break in for loop
                # when impossible
                return 0

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_arr = list(map(int, input().split()))
    print(f'#{t} {electric_bus(K, N, M, charge_arr)}')





