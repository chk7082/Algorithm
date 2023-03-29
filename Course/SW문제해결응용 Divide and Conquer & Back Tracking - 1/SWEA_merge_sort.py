def SWEA_merge_sort(start, end):
    '''
    merge sort (recursively)
    '''

    if start >= end:
        return

    # just to avoid overflow
    middle = start + (end+1-start)//2 - 1

    # proceed recursive step
    SWEA_merge_sort(start, middle)
    SWEA_merge_sort(middle+1, end)

    # count the number of cases when the last element of the left half
    # is greater than that of the right half
    if arr[middle] > arr[end]:
        count[0] += 1

    # merge the result
    left = start
    right = middle + 1
    tmp_to_store = start

    while left <= middle and right <= end:
        if arr[left] <= arr[right]:
            tmp[tmp_to_store] = arr[left]
            left += 1
        else:
            tmp[tmp_to_store] = arr[right]
            right += 1

        tmp_to_store += 1

    # when the left one left
    if left <= middle:
        while left <= middle:
            tmp[tmp_to_store] = arr[left]
            left += 1
            tmp_to_store += 1
    # when the right one left
    elif right <= end:
        while right <= end:
            tmp[tmp_to_store] = arr[right]
            right += 1
            tmp_to_store += 1

    # transform the information to the original arr
    # we need to consider from start to end
    for i in range(start, end + 1):
        arr[i] = tmp[i]

    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = [0]
    tmp = [-1] * N

    SWEA_merge_sort(0, N-1)

    print(f'#{t} {arr[N//2]} {count[0]}')
