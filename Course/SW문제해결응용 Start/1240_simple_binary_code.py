def simple_binary_code(N, M, code):
    '''
    function that determine whether the given code is valid or not
    and then return total sum of digits or 0 (resp)

    :param
    N, M (int) : positive integers representing the size of the code
    code (list) : list containing each row as string

    :return
    result (int) : total sum of digits, if it's valid
                                     0, otherwise
    '''

    # find the first row, whether the actual code appear
    for i in range(N):
        if '1' in code[i]:
            code_row = code[i]
            break

    # find the substring that consists the actual code (length 56)
    for j in range(M-1, -1, -1):
        if code_row[j] == '1':
            actual_code = code_row[j-55:j+1]
            break

    # initialize plain text
    plain_text = [-1] * 8

    for i in range(8):
        plain_text[i] = convertor[actual_code[7*i: 7*(i+1)]]

    # check validity
    # if it's not valid
    if (3 * sum(plain_text[::2]) + sum(plain_text[1::2])) % 10:
        return 0
    # if it's valid
    else:
        return sum(plain_text)


convertor = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
             '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
             '0110111': 8, '0001011': 9}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    code = [input() for _ in range(N)]

    print(f'#{t} {simple_binary_code(N, M, code)}')

