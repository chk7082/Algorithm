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
    return max(split_by_0)

# number of test cases
T = int(input())

for t in range(1, T+1):
    _ = int(input())
    num_string = input()
    print(f'#{t} {max_consecutive_num_of_1(num_string)}')





