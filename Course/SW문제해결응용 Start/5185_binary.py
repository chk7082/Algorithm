def hex_to_bin(N, hex_string):
    '''
    funciton that convert hexadecimal string to binary string

    :param
    N (int) : length of hex_string
    hex_string (str) : hexadecimal representation of given number

    :return:
    bin_string (str) : binary representation of given number
    '''

    bin_string = ''

    for char in hex_string:
        bin_string = bin_string + convertor[char]

    return bin_string


convertor = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
             '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
             'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())
for t in range(1, T+1):
    N, hex_string = input().split()
    N = int(N)

    print(f'#{t} {hex_to_bin(N, hex_string)}')