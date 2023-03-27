def array_partition_1(nums):
    '''
    function that compute the maximum special sum of
    given array nums

    (special sum)
    1. split nums array into len(nums)//2-many pairs
    2. for each pair compute minimum of them
    3. sum it -> special sum

    :param
    nums (list) : list containing numbers

    :return
    result (num) : the maximum special sum of
                   given array nums
    '''

    # sort it in descending order
    nums.sort(reverse=True)

    # it is equivalent to the choosing problem
    # where we should choose len(nums)//2 element of nums
    # with condition that for each chosen ith element,
    # the number of chosen elements in 0~ith <=
    # the number of un-chosen elements in 0~ith
    # then it can be automatically paired
    # alternating sequence will give us the best result
    return sum(nums[1::2])


nums = [1, 4, 3, 2]
print(array_partition_1(nums))
