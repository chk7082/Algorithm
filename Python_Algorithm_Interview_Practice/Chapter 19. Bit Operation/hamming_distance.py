def hamming_distance(x, y):
    '''
    function that return the hamming distance in binary representation
    between two integer x, y
    '''

    # it could be easily computed using xor operation
    return bin(x ^ y).count('1')


x = int('0b1011101', 2)
y = int('0b1001001', 2)
print(x, y) # 93 73
print(hamming_distance(x, y)) # 2