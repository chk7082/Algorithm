def sum_of_three_numbers(nums):
    '''
    function that return the list containing 3 elements of
    given list nums which sums up to 0

    :param
    nums (list) : list of numbers

    :return:
    result (list) : the list of list containing 3 elements of
                    given list nums which sums up to 0
                    (return -1, if impossible)
    '''

    # initialize our result
    result = []

    # sort nums
    # use the benefit of sorted array
    # with preprocessing cost of O(nlogn)
    nums.sort()

    # compute the length of nums
    L = len(nums)

    # focus on the lowest value among valid 3 elements
    # going to use 2-pointer
    for lowest_idx in range(0, L - 2):
        left = lowest_idx + 1
        right = L - 1

        # until it cross (or meet)
        while left < right:
            # current sum of two values where
            # indices left & right points at
            cur_sum = nums[lowest_idx] + nums[left] + nums[right]

            # if cur_sum == 0 (our target), return it
            if cur_sum == 0:
                # use tuple at this moment
                # for later purpose (deduplication)
                result.append((nums[lowest_idx], nums[left], nums[right]))

                # it could be possible that the
                # increase caused by left += 1
                # is equal to the
                # decrease caused by right -= 1
                left += 1
                right -= 1

            # if cur_sum < 0, move left index
            elif cur_sum < 0:
                left += 1

            # if cur_sum > 0, move right index
            else:
                right -= 1

    # use set for deduplication
    return list(map(list, set(result)))


nums = [-1, 0, 1, 2, -1, -4]
print(sum_of_three_numbers(nums))