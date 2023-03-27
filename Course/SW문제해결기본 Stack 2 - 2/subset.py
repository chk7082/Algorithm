def subset(i, N, target, previous_sum, possible_increment):
    '''
    function that compute the subsets of arr which sums up to target
    (recursively)

    :param
    i (int) : to denote we had been considered up to indices 0 ~ i-1
    N (int) : length of arr
    target (int) : our target
    previous_sum (int) : summation of all elements we have chosen from indices 0 ~ i-1
    possible_increment (int) : the maximum possible increment by choosing
                               all of the remaining ones i ~ N-1

    :return
    None, not going to return, just save it in result list
    '''

    # if it's equal to target
    if previous_sum == target:
        result.append([arr[k] for k in range(i)
                       if bits[k]])

    # when we don't need to consider further
    elif i == N: # when the sum is not equal to target, but we have considered all elements
        return
    elif previous_sum > target:
        return
    elif previous_sum + possible_increment < target:
        return

    # when we need to go further
    else:
        # when we include arr[i]
        bits[i] = 1
        subset(i + 1, N, target, previous_sum + arr[i], possible_increment - arr[i])

        # when we exclude arr[i]
        bits[i] = 0
        subset(i + 1, N, target, previous_sum, possible_increment - arr[i])


N = 10
arr = list(range(1, N + 1))
bits = [0] * N
result = []


subset(0, N, 10, 0, sum(arr))
print(result)