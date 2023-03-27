def single_numebr(nums):
    '''
    function that return the unique element in nums
    '''

    # since xor operation is associative & commutative
    # & xor with itself -> 0
    # & xor with 0 -> itself
    # just return the cumulative_xored_value of numbers in nums

    # initialize our object
    cumulative_xored_value = 0

    # for each element
    for num in nums:
        cumulative_xored_value ^= num

    return cumulative_xored_value


nums = [1, 6, 4, 6, 1, 7, 13, 4, 8, 13, 8]
print(single_numebr(nums)) # 7