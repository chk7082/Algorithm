def number_of_letters(str1, str2):
    '''
    function that return the alphabet in str1
    which is dominant in str2

    :param
    str1, str2 (str) : strings we're interested in

    :return
    result (str) : the alphabet in str1
                   which is dominant in str2
    '''

    # initialize our counter dictionary with char in str1
    dict_counter = {char : 0 for char in list(str1)}

    # count it
    for char in str2:
        # if str1 has char
        try:
            dict_counter[char] += 1
        except: # if not
            pass

    return max(dict_counter.values())



T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f'#{t} {number_of_letters(str1, str2)}')