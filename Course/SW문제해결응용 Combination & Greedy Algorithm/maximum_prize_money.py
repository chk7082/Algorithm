# def maximum_prize_money(nums, change_num):
#     '''
#     function that return the maximum winning prize money
#     that could be made by exactly swapping change_num times
#     '''
#
#     # pre-compute the sorted version
#     sorted_nums = sorted(nums, reverse=True)
#     L = len(nums)
#
#     # check if it has digits with multiplicity >= 2
#     if len(set(nums)) < L:
#         can_stay = True
#     else:
#         can_stay = False
#
#     # swap it (change_num) - times
#     for _ in range(change_num):
#         swap(nums, sorted_nums, L, can_stay)
#
#     # reconnect them
#     return int(''.join(nums))
#
#
# def swap(nums, sorted_nums, L, can_stay):
#     '''
#     one step of swapping
#     '''
#
#     # compare the given two list element-wisely
#     # it is sufficient to check it up to L-2
#     for i in range(L-1):
#         # if those two are different
#         if nums[i] != sorted_nums[i]:
#             index_different = i
#             break
#
#     # for-else, when it's already optimal
#     else:
#         # when we could just swap the same digit
#         if can_stay:
#             return
#         else:
#             # swap the last two ones
#             nums[-2], nums[-1] = nums[-1], nums[-2]
#             return
#
#     # find the index in nums that have value sorted_nums[index_different]
#     # when tie, use the largest one
#     for j in range(L-1, -1, -1):
#         if nums[j] == sorted_nums[index_different]:
#             # remember it
#             index_to_swap = j
#             break
#
#     # swap them
#     nums[index_to_swap], nums[index_different] = nums[index_different], nums[index_to_swap]
#     return


def f(cur_num, change_num, can_stay):
    if cur_num == change_num:
        record[0] = max(record[0], ''.join(nums))

        if nums == sorted_nums:
            found_optimal[0] = True

    elif found_optimal[0]:
        if can_stay:
            return
        else:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            f(cur_num + 1, change_num, can_stay)
            nums[-1], nums[-2] = nums[-2], nums[-1]

    else:
        for i in range(L-1):
            for j in range(i+1, L):
                nums[i], nums[j] = nums[j], nums[i]
                f(cur_num + 1, change_num, can_stay)
                nums[i], nums[j] = nums[j], nums[i]


def is_even_permutation(nums, sorted_nums, L):
    '''
    function that return True, if the given nums is even permutation of sorted version
    '''

    # initialize our object
    is_even = True

    while True:
        for i in range(L-1):
            if nums[i] != sorted_nums[i]:
                index_different = i
                break

        # for-else if those two are same
        else:
            return is_even

        # otherwise swap it
        is_even = not is_even

        # find the index in nums that have value sorted_nums[index_different]
        # when tie, use the largest one
        for j in range(L-1, -1, -1):
            if nums[j] == sorted_nums[index_different]:
                # remember it
                index_to_swap = j
                break

        # swap them
        nums[index_to_swap], nums[index_different] = nums[index_different], nums[index_to_swap]


T = int(input())
for t in range(1, T+1):
    nums, change_num = input().split()
    nums = list(nums)
    change_num = int(change_num)
    L = len(nums)

    # pre-compute the sorted version
    sorted_nums = sorted(nums, reverse=True)

    # check if it has digits with multiplicity >= 2
    if len(set(nums)) < L:
        can_stay = True
    else:
        can_stay = False

    record = ["0"*L]
    found_optimal = [False]
    if L <= change_num:
        if can_stay:
            record[0] = ''.join(sorted_nums)
        else:
            is_even = is_even_permutation(nums, sorted_nums, L)
            if is_even:
                record[0] = ''.join(sorted_nums)
            else:
                sorted_nums[-1], sorted_nums[-2] = sorted_nums[-2], sorted_nums[-1]
                record[0] = ''.join(sorted_nums)
    else:
        f(0, change_num, can_stay)

    print(f'#{t} {record[0]}')

