def new_bus_line(bus_type, A, B):
    '''
    function that return the maximum number of buses passing one bus stop

    :param
    bus_type (list) : collection of the types of bus
    A (list) : collection of the initial points
    B (list) : collection of the end points
               (all with synchronized order)

    :return
    result (int) : maximum number of buses passing one bus stop
    '''

    # storage for counting the multiplicity (index 0 : dummy)
    counts = [0] * 1001

    # for each bus
    for i in range(len(bus_type)):

        # configuration of current bus
        cur_bus_type = bus_type[i]
        start = A[i]
        end = B[i]

        # if normal
        # it visits every single bus stop from start to end
        if cur_bus_type == 1:
            counts[start : end+1] = map(lambda x: x+1, counts[start : end+1])

        # if express
        # alternation of visiting & non-visiting happens
        elif cur_bus_type ==2:
            counts[start : end+1 : 2] = map(lambda x: x+1, counts[start : end+1 : 2])

        # if global express
        else:
            # if start : odd
            if (start % 2):
                for i in range(start, end+1):
                    # if i is divisible by 3 and not disivible by 10
                    if (not (i % 3)) and (i % 10):
                        counts[i] += 1
            # if start : even
            else:
                # since 4 is even, we set step_size = 2
                for i in range(start, end+1, 2):
                    # if it is divisible by 4
                    if (not (i % 4)):
                        counts[i] += 1

    # return the maximum multiplicity
    return max(counts)

# number of test cases
T = int(input())

for t in range(1, T+1):
    N = int(input())

    # just for cumulation
    bus_type = []
    A = []
    B = []

    for _ in range(N):
        bus_type_i, A_i, B_i = map(int, input().split())
        bus_type.append(bus_type_i)
        A.append(A_i)
        B.append(B_i)

    print(f'#{t} {new_bus_line(bus_type, A, B)}')

