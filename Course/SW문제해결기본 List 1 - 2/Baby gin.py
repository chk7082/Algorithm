def Baby_gin(cards):
    '''
    function that return 1 if it's baby-gin, 0 otherwise
    (baby-gin : when cards are composed of only
    run(3 straight cards) & triple(3 equal cards))

    :param
    cards (list) : list of integers representing 6 cards

    :return:
    result (int) : 1 if baby-gin, 0 otherwise
    '''

    # the order of cards doesn't matter
    # we're gonna compute only the multiplicity of each cards
    # since the card lies in [0, 9]
    count = [0] * 10
    for card in cards:
        count[card] += 1

    # initialize result
    result = 1

    # if multiplicity >= 3 -> since len(cards) = 6,
    # 3 could only come from triple (assuming it's baby_gin)
    # first check the triples
    for i in range(len(count)):
        count[i] %= 3

    # check run
    for i in range(len(count)-2):
        cur_num = count[i]
        # if there is run (when 0,0,0 just continue, it's okay)
        if (count[i+1] >= cur_num) and (count[i+2] >= cur_num):
            count[i:i+3] = map(lambda x: x-cur_num, count[i:i+3])
        # if violate the condition
        else:
            result = 0

    return result

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
    your_input = input()
    print(f'#{t} {Baby_gin(string_to_digit_list(your_input))}')




