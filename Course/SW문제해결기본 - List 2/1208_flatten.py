def flatten(piled_boxes, dump_num):
    '''
    function that return the minimum difference between maximum_height and
    minimum height of piled boxes possibly after {dump_num}-many dump

    :param
    piled_boxes (list) : list of positive integers representing heights of
                         piled boxes
    :return:
    result (list) : minimum height difference after {dump_num}-many dump
    '''

    for _ in range(dump_num):
        # find max_val & min_val & corresponding indices
        max_val = max(piled_boxes)
        max_ind = piled_boxes.index(max_val)

        min_val = min(piled_boxes)
        min_ind = piled_boxes.index(min_val)

        # if it is already flat enough
        if max_val - min_val <= 1:
            print(max_val)
            print(min_val)
            return 1
        # if not
        else:
            # if our goal is just to flatten quickly
            # then I would rather change those max&min to their almost average
            # but not in this case
            # proceed 1 dump step
            piled_boxes[max_ind] -= 1
            piled_boxes[min_ind] += 1

    # if we used all dump_num chances
    return max(piled_boxes) - min(piled_boxes)

# number of test cases
T = 10

for t in range(1, T+1):
    dump_num = int(input())
    piled_boxes = list(map(int, input().split()))
    print(f'#{t} {flatten(piled_boxes, dump_num)}')

