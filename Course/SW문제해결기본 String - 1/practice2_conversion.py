def itoa(num):
    '''
    function that convert integer num to string
    (without str())

    :param
    num (int) : integer that we want to convert

    :return
    result (str) : converted string
    '''

    # initialize our result
    result = ''

    # until num is 0
    while num:
        # slicing effect
        num, remainder = divmod(num, 10)

        # concatenate it
        # ASCII 48 -> char 0
        result = chr(remainder + 48) + result

    return result

t = 1

while True:
    num = int(input())
    if num == -1:
        break
    string = itoa(num)
    print(f'#{t} {string} {type(string)}')
    t += 1


