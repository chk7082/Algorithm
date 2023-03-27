def string(str1, str2):
    '''
    function that return the number of substring in str2
    which is equal to str1

    :param
    str1, str2 (str) : strings that we want to check
                       the number of substring in str2
                       which is equal to str1

    :return:
    counts (int) : the number of substring in str2
                   which is equal to str1
    '''

    #initialize our object
    counts = 0

    # find the length of each string
    N = len(str1)
    M = len(str2)

    # for each possible start point of str2
    for start in range(M-N+1):
        # compare if str1 is exactly the same as substring of str2
        # with length M
        if str1 == str2[start : start+N]:
            counts += 1

    return counts



for _ in range(10):
    t = int(input())
    str1 = input()
    str2 = input()

    print(f'#{t} {string(str1, str2)}')