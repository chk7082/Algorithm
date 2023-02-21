def flickering_switch(L, state, query):
    '''
    function that return the state of switches after actions taken by query

    :param
    L (int) : the number of switches
    state (list) : state of switches
    query (list) : list containing the actions that we have to proceed

    :return
    state (list) : changed state of switches
    '''

    for gender, index in query:
        # if male
        if gender == 1:
            # switch it
            state[index: L+1: index] = map(lambda x: 1-x, state[index: L+1: index])

        # if female
        elif gender == 2:
            # figure out the interval
            increment = 1
            while state[index-increment] == state[index+increment]:
                increment += 1

            # switch it
            state[index - increment + 1: index + increment] = map(lambda x: 1-x, state[index - increment + 1: index + increment])

    num_of_lines = (L-1)//20 + 1
    for i in range(num_of_lines - 1):
        print(*state[1 + 20*i: 1 + 20*(i+1)])

    print(*state[1 + 20*(num_of_lines-1): -1])


L = int(input())
# -1 is just for the border
state = [-1] + list(map(int, input().split())) + [-1]

N = int(input())
query = []
for _ in range(N):
    query.append(list(map(int, input().split())))

flickering_switch(L, state, query)