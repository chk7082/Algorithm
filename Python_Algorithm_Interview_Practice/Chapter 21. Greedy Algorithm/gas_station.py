def gas_station(gas, cost):
    '''
    function that return the index of the starting point, if we could travel through all gas stations from there
                                                      -1, otherwise
    '''

    # when it's impossible
    if sum(gas) < sum(cost):
        return -1

    start = 0
    fuel = 0

    for i in range(len(gas)):
        increment = gas[i] - cost[i]
        if fuel + increment < 0:
            start = i + 1
        else:
            fuel += increment

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gas_station(gas, cost)) # 3