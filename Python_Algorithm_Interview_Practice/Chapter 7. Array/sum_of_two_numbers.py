def sum_of_two_numbers(nums, target):
    '''
    function that return the indices of two numbers in nums
    which sum up to target

    :param
    nums (list) : list of given numbers
    target (int) : our target

    :return
    [ind1, ind2] (list) : list containing two indices that we want
    '''

    # compute the length of nums
    L = len(nums)

    # brute force
    # if it finds one pair of [ind1, ind2], just return it
    for ind1 in range(L - 1):
        for ind2 in range(ind1 + 1, L):
            if nums[ind1] + nums[ind2] == target:
                return [ind1, ind2]


nums = [2, 7, 11, 15]
target = 9
print(sum_of_two_numbers(nums, target))

