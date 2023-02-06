def hyunju_box_change(N, Q, L, R):
    '''
    function that conduct hyunju's box change game

    :param
    N (int) : total number of boxes
    Q (int) : total number of actions
    L (list) : list containing the left bound of each actions
    R (list) : list containing the right bound of each actions

    :return
    result (list) : list of integers representing the result of the process
    '''

    # initialize result
    result = [0] * N

    # for each Q-many actions
    for i in range(Q):
        # conduct process
        result[L[i]-1:R[i]] = [i+1] * (R[i]-L[i]+1)

    return result

T = int(input())

for t in range(1, T+1):
    # N & Q
    N, Q = map(int, input().split())

    # L & R
    # cumulate L_i & R_i
    L = []
    R = []
    for _ in range(Q): # since we don't need index
        L_i , R_i = map(int, input().split())
        L.append(L_i)
        R.append(R_i)

    result = hyunju_box_change(N, Q, L, R)

    print(f'#{t}', end='')
    for element in result:
        print(f' {element}', end='')
    print()



