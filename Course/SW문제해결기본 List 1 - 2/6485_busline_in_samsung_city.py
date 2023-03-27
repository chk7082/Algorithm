def busline_in_samsumg_city(N, A, B, P):
    '''
    function that print total number of bus line for P-many bus stop

    :param
    N (int) : total number of bus line
    A (list) : lower bound for each bus line
    B (list) : upper bound for each bus line
    P (int) : number of bus stop that we want to calculate total number of bus line

    :return
    None, not gonna return, just print it
    '''

    # since index starts from 0, regard 0-index as dummy
    count = [0] * 5001

    # add +1 to where the ith bus goes
    for i in range(N):
        count[A[i]:B[i]+1] = [x + 1 for x in count[A[i]:B[i]+1]]

    for _ in range(P):
        query = int(input())
        print(f' {count[query]}', end='')

    return

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # cumulate A_i & B_i
    A = []
    B = []
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)

    P = int(input())
    print(f'#{t}', end='')
    busline_in_samsumg_city(N, A, B, P)
    print()