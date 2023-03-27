def maximum_sliding_window(nums, k):
    '''
    function that return the maximum_sliding_window
    '''

    # initialize the result
    result = [max(nums[:k])]

    for start in range(1, len(nums)-k+1):
        end = start + k

        # if the incoming one is greater than or equal to the previous max
        if nums[end-1] >= result[-1]:
            result.append(nums[end-1])

        # if the outgoing one is strictly less than the previous max
        elif nums[start-1] < result[-1]:
            result.append(result[-1])

        # otherwise we need to recompute it
        else:
            result.append(max(nums[start:end-1]))

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maximum_sliding_window(nums, k))