def seven_dwarf():
    '''
    function that print the seven dwarfs whose heights sums up to 100
    '''

    # input heights
    heights = [int(input()) for _ in range(9)]

    # we could always find such 7 dwarfs
    # compute our target (total_sum - 100)
    target = sum(heights) - 100

    # all we need to do is just to find two fake dwarfs
    # whose heights sums up to target
    # going to use two pointer
    left = 0
    right = 8

    # sort the heights
    heights.sort()

    while left < right:
        # compute current sum
        cur_sum = heights[left] + heights[right]

        if cur_sum == target:
            break
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

    for index in set(range(9)) - set([left, right]):
        print(heights[index])


seven_dwarf()