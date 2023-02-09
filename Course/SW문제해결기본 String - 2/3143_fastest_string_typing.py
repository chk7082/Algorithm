def fastest_string_typing(A, B):
    '''
    function that computes the minimum typing number
    to make string A with using shortcut of string B

    :param
    A (str) : string that we want to type
    B (str) : special message that we could type in shortcut(in 1 typing)

    :return
    result (int) : minimum typing number to make string A
                   with using shortcut of string B
    '''

    # initialize counts which will contain
    # the maximum number of disjoint Bs in A
    counts = 0

    # i : index of A
    i = 0

    # length of A & B
    A_length = len(A)
    B_length = len(B)

    # until break
    while i < A_length:
        # if we find one starts at index i, we don't need to consider
        # index i ~ i + B_length - 1
        # in this greedy way(count it from the first), we could find counts
        if A[i:i+B_length] == B:
            i += B_length
            counts += 1

        # else move i
        else:
            i += 1

    return A_length + (1 - B_length) * counts


T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    print(f'#{t} {fastest_string_typing(A, B)}')