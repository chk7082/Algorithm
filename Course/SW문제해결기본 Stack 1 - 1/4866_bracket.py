def bracket(original_string):
    '''
    function that return 1, if it's valid parenthesis
                         0, otherwise

    :param
    original_string (str) : original string consists of parenthesis &
                            possibly other characters

    :return
    result (int) : 1, if it's grammatically correct parenthesis
                   0, otherwise
    '''

    # extract only parenthesis in original_string
    string = ''.join([char for char in original_string
                      if char in ('(', '{', '[', ')', '}', ']')])

    # initialize top
    top = -1

    def push(stack, item, size):
        nonlocal top
        top += 1
        if top == size:
            # print('overflow!')
            top -= 1
            # raise
        else:
            stack[top] = item

    def pop(stack):
        nonlocal top
        if top == -1:
            # print('underflow!')
            raise
        else:
            top -= 1
            return stack[top + 1]

    # length of string
    L = len(string)

    # current stack to keep track parenthesis
    parenthesis_stack = [''] * L

    # convertor (closing parenthesis to opening parenthesis)
    convertor = {')': '(', '}': '{', ']': '['}

    for char in string:
        # if it's opening parenthesis
        if char in ('(', '{', '['):
            # in push operation, overflow can't occur
            # since we use size to len(string)
            push(parenthesis_stack, char, L)

        # if it's closing parenthesis
        elif char in (')', '}', ']'):
            try:
                last_element = pop(parenthesis_stack)

                # if it's not equal the last element of stack
                if last_element != convertor[char]:
                    return 0
            # when closing parenthesis precede the opening one
            except:
                return 0

        # if it's not one of parenthesis
        else:
            return 0

    # if there's remaining parenthesis
    if top >= 0:
        return 0
    # when it's valid
    else:
        return 1


T = int(input())
for t in range(1, T+1):
    string = input()
    print(f'#{t} {bracket(string)}')