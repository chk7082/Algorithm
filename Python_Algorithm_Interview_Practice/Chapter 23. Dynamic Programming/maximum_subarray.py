def maximum_subarray(arr):
    '''
    function that return the summation of consecutive subarray that maximize
    their sum
    '''

    # initialization step
    best_sum = -1e8
    cur_sum = 0

    # Kadane's Algorithm
    for num in arr:
        cur_sum = max(cur_sum+num, num)
        best_sum = max(best_sum, cur_sum)

    return best_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray(arr))