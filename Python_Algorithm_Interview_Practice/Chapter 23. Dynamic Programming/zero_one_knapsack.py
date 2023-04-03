def zero_one_knapsack(cargo, N, capacity):
    '''
    function that solve the zero_one_knapsack problem given cargo &
    N : the number of items & capacity : limit of the bag
    '''

    # initialize the table to record the solution of sub-problems
    # record : matrix of size (N+1) by (capacity+1)
    #          where the element in ith row & jth column denote the solution
    #          when considering the first i-many cargo & capacity j
    record = [[0]*(capacity+1) for _ in range(N+1)]

    # determine each elements in the tables
    for i in range(1, N+1):
        for j in range(1, capacity+1):
            # initialize our candidate
            candidate = [record[i-1][j]]

            # consider when we include i-th item (cargo[i-1])
            if j-cargo[i-1][1] >= 0:
                candidate.append(record[i-1][j-cargo[i-1][1]] + cargo[i-1][0])

            # determine record[i][j]
            record[i][j] = max(candidate)

    return record[-1][-1]



N = 5
cargo = [(4, 12),  # index of items starts from 0
         (2, 1),
         (10, 4),
         (1, 1),
         (2, 2),
         ]
capacity = 15

r = zero_one_knapsack(cargo, N, capacity)
print(r)