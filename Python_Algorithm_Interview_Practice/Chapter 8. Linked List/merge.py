def merge(List1, List2):
    '''
    function that merge given List1 & List2 (in increasing order)

    :param
    List1, List2 (list) : given List1 & List2 that we want to merge

    :return
    result (list) : sorted list (in increasing order)
    '''

    # length of List1 & List2
    L1, L2 = len(List1), len(List2)

    # initialize our object & indices
    result = []
    index1 = 0
    index2 = 0

    # until there's remaining one in both Lists
    while index1 < L1 and index2 < L2:
        # if one from List1 is smaller than one from List2
        if List1[index1] < List2[index2]:
            result.append(List1[index1])
            index1 += 1
        # otherwise
        else:
            result.append(List2[index2])
            index2 += 1

    # when we've finished one List
    if index1 == L1:
        result.extend(List2[index2:])
    else:
        result.extend(List1[index1:])

    return result


List1 = '1->2->4'.split('->')
List2 = '1->3->4'.split('->')
combined_List = merge(List1, List2)
print('->'.join(combined_List))

