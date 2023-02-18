def cutting_iron_bar(string_rep):
    '''
    function that return the total number of iron bars split by laser

    :param
    string_rep (str) : string representation of laser & iron bar

    :return:
    result (int) : the total number of iron bars split by laser
    '''

    # initialize our result
    result = 0

    # convert adjacent '()' to char '1' (just to denote laser)
    converted_string = string_rep.replace('()', '1')

    # assume we're using stack
    # but we don't need to store every element in stack
    # just maintain top index (as if we're using stack)
    top = -1

    # for each char in converted_string
    for char in converted_string:
        # when (, push
        if char == '(':
            top += 1

            # since we got new one
            result += 1

        elif char == ')':
            top -= 1

        # if it's laser
        else:
            result += (top + 1)

    return result


T = int(input())
for t in range(1, T+1):
    string_rep = input()
    print(f'#{t} {cutting_iron_bar(string_rep)}')