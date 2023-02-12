def product_of_array_except_self(nums):
    '''
    function that compute the product of array except self

    :param
    nums (list) : list containing numbers

    :return
    result (list) : list containing the product of array except self
                    len(result) == len(nums) &
                    result[i] = (product of elements
                    in nums except for nums[i])
    '''

    # use cumulative product
    # one starting from the left
    # and the other one starting from the right

    # initialize our result
    L = len(nums)
    result = [1] * L

    # cumulative product except itself
    cum_product = 1

    # one starting from the left
    for i in range(1, L):
        cum_product *= nums[i-1]
        result[i] *= cum_product

    # one starting from the right
    cum_product = 1
    for i in range(L-2, -1, -1):
        cum_product *= nums[i+1]
        result[i] *= cum_product

    return result


nums = [1, 2, 3, 4]
print(product_of_array_except_self(nums))