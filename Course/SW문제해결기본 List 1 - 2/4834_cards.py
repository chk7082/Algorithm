def cards(card_list):
    '''
    function that return the maximum number of digits and corresponding numbers
    (if tie occurs -> print higher num)

    :param
    card_list (list) : list of integers containing digits

    :return:
    (digit, max_multiplicity) (tuple) : tuple containing digit and
                                        its maximum multiplicity
    '''

    # counting storage (0 ~ 9)
    count = [0] * 10

    # count it
    for card in card_list:
        count[card] += 1

    # initialize our result
    max_multiplicity = -1
    digit = -1

    for i in range(len(count)-1, -1, -1):
        # record renewal step
        if count[i] > max_multiplicity:
            # update it
            max_multiplicity = count[i]
            digit = i

    return (digit, max_multiplicity)


def string_to_digit_list(string):
    '''
    function that convert string representing cards to list of cards

    :param
    string (str) : string that represent cards

    :return:
    result (list) : list of digits containing cards
    '''
    return list(map(int, list(string)))

T = int(input())
for t in range(1, T+1):
    # we don't need N
    _ = input()

    # test digits (string)
    string = input()
    result = cards(string_to_digit_list(string))
    print(f'#{t} {result[0]} {result[1]}')