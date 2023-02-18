def helper_calculator(operand1, operand2, operator):
    '''
    helper function that compute operation of operand 1 & 2

    :param
    operand1 (num) : first operand
    operand2 (num) : second operand
    operator (str) : string representing one of 4 basic operations
                     '+', '-', '*', '/'

    :return
    result (num) : operation result
    '''

    operand1 = int(operand1)
    operand2 = int(operand2)

    if operator == '+':
        return str(operand1 + operand2)
    elif operator == '-':
        return str(operand1 - operand2)
    elif operator == '*':
        return str(operand1 * operand2)
    elif operator == '/':
        return str(operand1 / operand2)


T = 10

for t in range(1, T+1):
    _ = int(input())
    infix = input()
    stack = []
    result = ''

    # 공백일경우 굳이 처음에 빼지 말고 그냥 나올때 처리를 안하면 될듯

    # 변환할 식을 순회
    ###############################################################
    ################# conversion step #############################
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stack에 push
            if not stack: # if len(stack) == 0
                stack.append(token)

            # stack이 비어있지 않은 경우, 우선순위에 따라야겠다
            else:
                # (는 incoming 우선순위가 가장 높음
                if token == '(':
                    stack.append(token)
                # )는 (가 나올때까지 stack에서 pop, result에 append
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    # (가 나오면 그냥 버리기
                    stack.pop()

                # incoming 우선순위가 2인 경우
                elif token == '*' or token == '/':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack에서 pop, result에 append
                    while stack and (stack[-1] == '*' or stack[-1] == '/'):
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+' or token == '-':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    ###############################################################
    ################# computing step ##############################

    # initialize stack for computing step
    stack = []

    # operand : 0 ~ 9 in this case
    # use the result of above (conversion step)
    for token in result:
        # if it's operand
        if token.isdigit():
            stack.append(token)

        # if it's operator
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(helper_calculator(operand1, operand2, token))

    print(f'#{t} {stack[-1]}')
