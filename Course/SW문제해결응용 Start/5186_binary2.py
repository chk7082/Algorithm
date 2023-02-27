def decimal_to_binary(num):
    '''
    function that convert decimal number in (0, 1)
    to binary representation (under decimal point)

    if we could represent it in 12 digits -> return it
    otherwise -> return 'overflow'

    :param
    num (int) : decimal number in (0, 1)

    :return
    result (str) : binary representation under decimal point, if it can be represented in 12 digits
                                                  'overflow', otherwise
    '''

    # initialization
    cur_length = 0
    result = ''

    while True:
        # update cur_length
        cur_length += 1

        # if it's exactly the same
        if num == 0:
            return result

        # if overflow
        elif cur_length == 13:
            return 'overflow'

        # update it
        num *= 2

        # determine current bit
        if num >= 1:
            num -= 1
            result = result + '1'
        else:
            result = result + '0'


T = int(input())
for t in range(1, T+1):
    num = float(input())

    print(f'#{t} {decimal_to_binary(num)}')