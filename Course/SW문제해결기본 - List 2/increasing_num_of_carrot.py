# will use SWEA 9386 just for convenience
def max_consecutive_num_of_1(num_string):
    '''
    function that return the maximum number of consecutive 1 in num_string

    :param
    num_string (string) : string that contains binary bits

    :return
    result (int) : integer that represent the maximum consecutive
                   number of 1 in num_string
    '''

    # split the num_string by delimiter '0'
    split_by_0 = num_string.split('0')

    # compute length of each elements
    split_by_0 = list(map(lambda x:len(x), split_by_0))

    # return maximum of them
    return max(split_by_0) + 1

def carrot_to_binary_convertor(carrots, N):
    '''
    function that convert carrots to binary bits which is compatible to
    max_consecutive_num_of_1 above

    :param
    carrots (list) : list containing the size of carrots

    :return
    result (string) : string consist of 0, 1 which is compatible to
                      number of 1 in num_string function above
                      (1, if it is greather than previous one,
                      0, otherwise)
    '''

    # initialize our result
    result = '0'

    for i in range(1, N): # excluding the first index 0
        if carrots[i] > carrots[i-1]:
            result += '1'
        else:
            result += '0'

    return result

# number of test cases
T = int(input())

for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    # actually we have modified max_consecutive_num_of_1 to return 1 added value
    # to consider beginning one
    # and initialized result = '0' in carrot_to_binary_convertor fn
    # to make consistant result
    print(f'#{t} {max_consecutive_num_of_1(carrot_to_binary_convertor(carrots, N))}')
