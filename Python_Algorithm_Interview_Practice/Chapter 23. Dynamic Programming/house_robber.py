def house_robber(money):
    '''
    function that return the maximum amount of money that the robber could possibly get
    '''

    # initialize the record table that will remember the sub-problem
    # where i-th element of it consider only the first i-many houses
    L = len(money)
    record = [0]*L
    record[0] = money[0]
    record[1] = max(money[0], money[1])

    for i in range(2, L):
        record[i] = max(record[i-1], record[i-2]+money[i])

    return record[-1]


# money = [1, 2, 3, 1]
money = [2, 7, 9, 3, 1]

print(house_robber(money))  # 12
