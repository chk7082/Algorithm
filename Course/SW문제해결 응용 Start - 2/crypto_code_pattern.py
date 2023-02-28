import sys
sys.stdin = open('input.txt')


def crypto_code_pattern(N, M, original_code):
    '''
    function that determine whether the given code is valid or not
    and then return total sum of digits or 0 (resp)

    :param
    N (int) : number of rows in total_code
    M (int) : number of cols in total_code (string length of each elements of original_code)
    original_code (list) : original code containing encrypted message
                           (in hexadecimal)

    :return
    total_sum (int) : total sum of digits, if it's valid
                                        0, otherwise
    '''

    # initialize our object
    total_sum = 0
    recent_i = 0

    # until there's no remaining code
    while True:
        # find the actual row that contains cipher text
        found = 0
        for i in range(max(0, recent_i), N):
            if found:
                break

            for j in range(M - 1, -1, -1):
                if original_code[i][j] != '0':
                    # remember the coordinate
                    x, y = i, j
                    actual_row = original_code[i]
                    found = 1
                    recent_i = i
                    break
        # for-else
        # if there's no remaining cipher text
        else:
            return total_sum

        # find the magnitude
        binary_row = actual_row.rstrip('0')
        switch_num = 0
        prev = '1'
        cur_length = len(binary_row)
        for j in range(cur_length-1, -1, -1):
            if switch_num == 4:
                magnitude = round((cur_length-j) / 7)
                break

            elif binary_row[j] != prev:
                switch_num += 1
                prev = binary_row[j]

        # extract cipher text
        cipher_text = binary_row[-1-55*magnitude::magnitude]

        # initialize plain text
        plain_text = [-1] * 8

        for i in range(8):
            plain_text[i] = convertor[cipher_text[7 * i: 7 * (i + 1)]]

        # check validity
        # if it's valid
        if not (3 * sum(plain_text[::2]) + sum(plain_text[1::2])) % 10:
            total_sum += sum(plain_text)

        # erase the current ciphertext
        height = 0
        while True:
            height += 1

            if original_code[x + height][y] == '0':
                break

        for i in range(x, x+height):
            original_code[i] = original_code[i][:y-56*magnitude+1] + '0'*(56*magnitude) + original_code[i][y+1:]



# def hex_to_bin(string):
#     '''
#     function that convert hexadecimal string to binary string
#     '''
#
#     return bin(int('0x'+string, 16))[2:].zfill(4)


convertor = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
             '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
             '0110111': 8, '0001011': 9}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    original_code = [bin(int('0x' + input(), 16))[2:].zfill(4*M) for _ in range(N)]

    print(f'#{t} {crypto_code_pattern(N, 4 * M, original_code)}')