def helper_calculator(operand1, operand2, operator):
    '''
    helper function that compute operation of operand 1 & 2

    :param
    operand1 (int) : first operand
    operand2 (int) : second operand
    operator (str) : string representing one of 4 basic operations
                     '+', '-', '*', '/'

    :return
    result (int) : operation result
    '''

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 // operand2


def forth_calculator(string):
    '''
    function that compute the postfix expression given by string

    :param
    string (str) : postfix expression

    :return
    result (str) : resulting number in string format
    '''
    # initialize stack for computing step
    stack = []

    for token in string.split():

        # if it's negative operand
        if len(token) > 1 and token[0] == '-' and token[1:].isdigit():
            stack.append(int(token))

        # if it's operand
        elif token.isdigit():
            stack.append(int(token))

        # if it's operator
        elif token in ('+', '-', '*', '/'):
            # if stack doesn't have enough elements, error
            if len(stack) <= 1:
                return 'error'

            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(helper_calculator(operand1, operand2, token))

    if len(stack) > 1:
        return 'error'

    return stack.pop()


T = int(input())

for t in range(1, T+1):
    string = input()
    print(f'#{t} {forth_calculator(string)}')
