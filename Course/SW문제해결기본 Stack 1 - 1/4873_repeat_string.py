def repeat_string(string):
    '''
    function that return the length of new string
    where new string is made by consecutive deleting of repeated characters
    (until possible)

    :param
    string (str) : original string that we want to delete repeated characters

    :return
    result (int) : the length of new string
    '''

    # if empty string, just return
    L = len(string)
    if not len(string):
        print('empty string, just return')
        return

    # initialize stack & top
    # we're going to stack the characters that we want
    stack = ['']*L
    top = -1

    # for each char in string
    for char in string:
        # None, if stack is empty
        # previous char, otherwise
        prev_char = None if top==-1 else stack[top]

        # if it's equal to previous one (repeated)
        # pop it in the stack
        if prev_char == char:
            top -= 1

        # otherwise, push it (non-repeated word)
        else:
            top += 1
            stack[top] = char

    # variable top maintain the length of new string
    return top + 1


T = int(input())
for t in range(1, T+1):
    string = input()
    print(f'#{t} {repeat_string(string)}')



