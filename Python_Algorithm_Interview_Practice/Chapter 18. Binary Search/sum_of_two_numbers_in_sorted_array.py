def sum_of_two_numbers_in_sorted_array(numbers, target):
    '''
    function that return the indices of two elements,
    which sum up to target in numbers list
    '''

    # pre-compute the length of the numbers list
    L = len(numbers)

    for i in range(L):
        left = i
        right = L - 1

        remainder = target - numbers[i]

        while left <= right:
            mid = left + (right - left)//2

            if numbers[mid] == remainder:
                return [i + 1, mid + 1]
            elif numbers[mid] < remainder:
                left = mid + 1
            else:
                right = mid - 1


numbers = [2, 7, 11, 15]
target = 9

print(sum_of_two_numbers_in_sorted_array(numbers, target))