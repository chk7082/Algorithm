def string_comparison(str1, str2):
    '''
    function that return 1, if str1 is substring of str2
                         0, otherwise

    :param
    str1, str2 (str) : strings that we want to check
                       if str1 is substring of str2 or not

    :return:
    result (int) : 1, if str1 is substring of str2
                   0, otherwise
    '''

    # find the length of each string
    N = len(str1)
    M = len(str2)

    # for each possible start point of str2
    for start in range(M-N+1):
        # compare if str1 is exactly the same as substring of str2
        # with length M
        if str1 == str2[start : start+N]:
            return 1
    else: # for-else
        return 0


T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{t} {string_comparison(str1, str2)}')