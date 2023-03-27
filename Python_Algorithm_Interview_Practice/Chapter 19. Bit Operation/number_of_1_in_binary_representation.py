def number_of_1_in_binary_representation(num):
    '''
    function that return the number of 1 in binary representation of num
    (num : unsigned integer)
    '''

    # initialize our object
    total_number_of_1 = 0

    # until 0
    while num:
        # if least significant bit is 1
        # count it
        if num & 1:
            total_number_of_1 += 1

        # shift it (equal to //= 2)
        num >>= 1

    return total_number_of_1


num = int('0b11111111111111111111111111111101', 2)
print(num) # 4294967293

print(number_of_1_in_binary_representation(num)) # 31

