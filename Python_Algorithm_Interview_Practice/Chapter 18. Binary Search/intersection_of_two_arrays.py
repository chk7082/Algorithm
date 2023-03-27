def intersection_of_two_arrays(nums1, nums2):
    '''
    function that return the intersection of two lists nums1 & nums2
    '''

    # sort the latter one
    nums2_sorted = sorted(nums2)

    # initialize our object
    result = set()
    L = len(nums2)

    # for each num in nums1
    for num in nums1:
        left = 0
        right = L - 1

        # binary search step
        while left <= right:
            mid = left + (right - left)//2

            if nums2_sorted[mid] == num:
                # if it's also in nums2
                # add it to our intersection result
                # and then break
                result.add(num)
                break
            elif nums2_sorted[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

    return list(result)




nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

print(intersection_of_two_arrays(nums1, nums2))